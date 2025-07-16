import os
import mimetypes
from datetime import datetime
from rename_media_files.config.config import FileMetadata, datetime_format

# Add imports for EXIF and pymediainfo
from exifread import process_file as exif_process_file
from pymediainfo import MediaInfo

class MediaFilesModel:
    def __init__(self, files: list[str]):
        self.files = files
        self.metadata_list = [self._create_metadata(file_path) for file_path in files]

    def _create_metadata(self, file_path: str) -> FileMetadata:
        mime_type, _ = mimetypes.guess_type(file_path)
        file_type = self._get_file_type(mime_type)
        creation_date = self._get_creation_date(file_path, mime_type)
        modification_date = self._get_modification_date(file_path)
        return FileMetadata(
            file_path=file_path,
            creation_date=creation_date,
            modification_date=modification_date,
            file_type=file_type,
            mime_type=mime_type or "unknown"
        )

    def _get_file_type(self, mime_type: str | None) -> str:
        if mime_type is None:
            return "unknown"
        if mime_type.startswith("image"):
            return "image"
        if mime_type.startswith("video"):
            return "video"
        if mime_type.startswith("audio"):
            return "audio"
        return "other"

    def _get_creation_date(self, file_path: str, mime_type: str | None) -> str:
        # For images, try EXIF
        if mime_type and mime_type.startswith("image"):
            try:
                with open(file_path, "rb") as f:
                    tags = exif_process_file(f, details=False)
                date_tag = tags.get("EXIF DateTimeOriginal") or tags.get("Image DateTime")
                if date_tag:
                    # EXIF date format: "YYYY:MM:DD HH:MM:SS"
                    dt = datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S")
                    return dt.strftime(datetime_format)
            except Exception as e:
                print(f"EXIF read error for {file_path}: {e}")  # Print error before fallback

        # For audio/video, try pymediainfo
        if mime_type and (mime_type.startswith("video") or mime_type.startswith("audio")):
            try:
                media_info = MediaInfo.parse(file_path)
                for track in media_info.tracks:
                    for attr in ["encoded_date", "tagged_date"]:
                        dt_str = getattr(track, attr, None)
                        if dt_str:
                            # Remove 'UTC' from anywhere and strip whitespace
                            dt_str = dt_str.replace("UTC", "").strip()
                            try:
                                dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                                return dt.strftime(datetime_format)
                            except Exception as e:
                                print(f"Date parse error for {file_path} ({attr}): {e}")
            except Exception as e:
                print(f"MediaInfo read error for {file_path}: {e}")  # Print error before fallback

        # Fallback: file system creation time
        print(f"Using file system creation time for {file_path}")
        ts = os.path.getctime(file_path)
        return datetime.fromtimestamp(ts).strftime(datetime_format)

    def _get_modification_date(self, file_path: str) -> str:
        ts = os.path.getmtime(file_path)
        return datetime.fromtimestamp(ts).strftime(datetime_format)

    @property
    def metadata(self) -> list[FileMetadata]:
        return self.metadata_list