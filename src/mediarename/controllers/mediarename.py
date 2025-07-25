import os
from typing import List
from mediarename.config.config import AppArgs, FileMetadata
from mediarename.models.media_files_model import MediaFilesModel
from mediarename.views.metadata_printer import print_metadata_list
from mediarename.models.rename_files import rename_files, pretend_rename_files


__all__ = ['main']


def get_files_from_input(input_path: str) -> list[str]:
    """
    Get a list of file paths from the input path.

    Args:
        input_path (str): Path to a file or directory.

    Returns:
        list[str]: List of file paths. If input is a file, returns a single-element list.
                   If input is a directory, returns all files in the directory.
                   Returns an empty list if input is invalid.
    """
    if os.path.isfile(input_path):
        return [input_path]
    elif os.path.isdir(input_path):
        return [
            os.path.join(input_path, f)
            for f in os.listdir(input_path)
            if os.path.isfile(os.path.join(input_path, f))
        ]
    else:
        print(f"Input path '{input_path}' is not a valid file or directory.")
        return []


def main(args: AppArgs) -> None:
    """
    Main entry point for processing and renaming media files.

    Args:
        args (AppArgs): Application arguments containing input path and options.

    Returns:
        None
    """
    input: str = args["input"]
    datetime_format: str = args["datetime_format"]

    files: List[str] = get_files_from_input(input)
    media_files_model: MediaFilesModel = MediaFilesModel(files, datetime_format)
    media_files_metadata: List[FileMetadata] = media_files_model.metadata

    if media_files_metadata and args.get("verbose", False):
        print_metadata_list(media_files_metadata)

    # Invoke renaming after metadata is available
    if media_files_metadata:
        if args.get("dry_run", False):
            print("Dry run mode: No files will be renamed.")
            pretend_rename_files(media_files_metadata)
        else:
            print("Renaming files...")
            rename_files(media_files_metadata)

    return None
