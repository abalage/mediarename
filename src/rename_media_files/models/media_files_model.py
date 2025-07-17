import os
import mimetypes
from datetime import datetime
from rename_media_files.config.config import FileMetadata
from exifread import process_file as exif_process_file
from pymediainfo import MediaInfo


class MediaFilesModel:
    """Model for extracting and storing metadata from media files."""

    def __init__(self, files: list[str], datetime_format: str) -> None:
        """
        Initialize the MediaFilesModel with a list of file paths.

        Args:
            files (list[str]): List of media file paths.
            datetime_format (str): Format for datetime strings in filenames.
        """
        forbidden_chars = set(r'\/:*?"<>|;')
        if any(c in datetime_format for c in forbidden_chars):
            raise ValueError(
                f"datetime_format contains forbidden characters: {forbidden_chars & set(datetime_format)}"
            )
        self.files = files
        self.datetime_format = datetime_format
        self.metadata_list = [self._create_metadata(file_path) for file_path in files]

    def _create_metadata(self, file_path: str) -> FileMetadata:
        """
        Create FileMetadata for a given file path.

        Args:
            file_path (str): Path to the media file.

        Returns:
            FileMetadata: Metadata object for the file.
        """
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
        """
        Determine the file type from the MIME type.

        Args:
            mime_type (str | None): MIME type string.

        Returns:
            str: File type ('image', 'video', 'audio', or 'other').
        """
        if mime_type is None:
            return "unknown"
        if mime_type.startswith("image"):
            return "image"
        if mime_type.startswith("video"):
            return "video"
        if mime_type.startswith("audio"):
            return "audio"
        return "other"

    def _get_image_creation_date(self, file_path: str) -> str | None:
        """
        Extract the creation date from image EXIF metadata.

        Args:
            file_path (str): Path to the image file.

        Returns:
            str | None: Creation date string if available, else None.
        """
        try:
            with open(file_path, "rb") as f:
                tags = exif_process_file(f, details=False, extract_thumbnail=False)
            date_tag = tags.get("EXIF DateTimeOriginal") or tags.get("Image DateTime")
            if date_tag:
                dt = datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S")
                return dt.strftime(self.datetime_format)
        except Exception as e:
            print(f"EXIF read error for {file_path}: {e}")
        return None

    def _get_media_creation_date(self, file_path: str) -> str | None:
        """
        Extract the creation date from video/audio metadata.

        Args:
            file_path (str): Path to the media file.

        Returns:
            str | None: Creation date string if available, else None.
        """
        try:
            media_info = MediaInfo.parse(file_path)
            for track in media_info.tracks:
                for attr in ["encoded_date", "tagged_date"]:
                    dt_str = getattr(track, attr, None)
                    if dt_str:
                        dt_str = dt_str.replace("UTC", "").strip()
                        try:
                            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                            return dt.strftime(self.datetime_format)
                        except Exception as e:
                            print(f"Date parse error for {file_path} ({attr}): {e}")
        except Exception as e:
            print(f"MediaInfo read error for {file_path}: {e}")
        return None

    def _get_creation_date(self, file_path: str, mime_type: str | None) -> str:
        """
        Get the creation date for a file, preferring metadata over file system timestamps.

        Args:
            file_path (str): Path to the media file.
            mime_type (str | None): MIME type string.

        Returns:
            str: Creation date string.
        """
        if mime_type:
            if mime_type.startswith("image"):
                date = self._get_image_creation_date(file_path)
                if date:
                    return date
            elif mime_type.startswith("video") or mime_type.startswith("audio"):
                date = self._get_media_creation_date(file_path)
                if date:
                    return date

        # Fallback: file system modification time
        print(f"Using file system modification time for {file_path}")
        return self._get_modification_date(file_path)

    def _get_modification_date(self, file_path: str) -> str:
        """
        Get the modification date for a file from the file system.

        Args:
            file_path (str): Path to the media file.

        Returns:
            str: Modification date string.
        """
        ts = os.path.getmtime(file_path)
        return datetime.fromtimestamp(ts).strftime(self.datetime_format)

    @property
    def metadata(self) -> list[FileMetadata]:
        """
        List of FileMetadata objects for all files.

        Returns:
            list[FileMetadata]: List of metadata objects.
        """
        return self.metadata_list
