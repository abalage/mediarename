import os
from typing import List
from rename_media_files.config.config import FileMetadata


def rename_files(media_files_metadata: List[FileMetadata]) -> None:
    """
    Rename media files based on their creation date metadata.

    Args:
        media_files_metadata (List[FileMetadata]): List of FileMetadata objects containing file paths and metadata.

    Returns:
        None
    """
    for metadata in media_files_metadata:
        dt_str: str = metadata.creation_date
        ext: str = os.path.splitext(metadata.file_path)[1]
        new_name: str = f"{dt_str}{ext}"
        src: str = metadata.file_path
        # Always use the original directory
        dst_dir: str = os.path.dirname(src)
        dst: str = os.path.join(dst_dir, new_name)

        # Skip if already renamed
        if os.path.basename(src) == new_name:
            print(f"Already renamed: {src}")
            continue

        try:
            os.rename(src, dst)
            print(f"Renamed: {src} -> {dst}")
        except Exception as e:
            print(f"Rename failed for {src}: {e}")
