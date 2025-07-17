from typing import List
from rename_media_files.config.config import FileMetadata


class MetadataPrinter:
    """Utility class for printing metadata information of media files."""

    def __init__(self, metadata_list: List[FileMetadata]):
        """
        Initialize with an iterable of FileMetadata objects.
        """
        self.metadata_list = metadata_list

    def print_file_paths(self) -> None:
        """Print file paths of all metadata entries."""
        for metadata in self.metadata_list:
            print(f"File: {getattr(metadata, 'file_path', 'N/A')}")

    def print_metadata_list(self) -> None:
        """Print detailed metadata for each file."""
        for metadata in self.metadata_list:
            print(f"File: {getattr(metadata, 'file_path', 'N/A')}")
            print(f"  Creation date: {getattr(metadata, 'creation_date', 'N/A')}")
            print(f"  Modification date: {getattr(metadata, 'modification_date', 'N/A')}")
            print(f"  File type: {getattr(metadata, 'file_type', 'N/A')}")
            print(f"  MIME type: {getattr(metadata, 'mime_type', 'N/A')}")
