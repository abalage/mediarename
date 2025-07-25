from typing import List
from mediarename.config.config import FileMetadata


def print_file_paths(metadata_list: List[FileMetadata]) -> None:
    """Print file paths of all metadata entries."""
    for metadata in metadata_list:
        print(f"File: {getattr(metadata, 'file_path', 'N/A')}")


def print_metadata_list(metadata_list: List[FileMetadata]) -> None:
    """Print detailed metadata for each file."""
    for metadata in metadata_list:
        print(f"File: {getattr(metadata, 'file_path', 'N/A')}")
        print(f"  Creation date: {getattr(metadata, 'creation_date', 'N/A')}")
        print(f"  Modification date: {getattr(metadata, 'modification_date', 'N/A')}")
        print(f"  File type: {getattr(metadata, 'file_type', 'N/A')}")
        print(f"  MIME type: {getattr(metadata, 'mime_type', 'N/A')}")
