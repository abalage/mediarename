import os
from typing import List
from rename_media_files.config.config import AppArgs, FileMetadata
from rename_media_files.models.media_files_model import MediaFilesModel
from rename_media_files.views.metadata_printer import MetadataPrinter
from rename_media_files.models.rename_files import rename_files


__all__ = ['main']


def get_files_from_input(input_path: str) -> list[str]:
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
    input: str = args["input"]

    files: List[str] = get_files_from_input(input)
    media_files_model: MediaFilesModel = MediaFilesModel(files)
    media_files_metadata: List[FileMetadata] = media_files_model.metadata

    if media_files_metadata and args.get("verbose", False):
        metadata_printer: MetadataPrinter = MetadataPrinter(media_files_metadata)
        metadata_printer.print_metadata_list()

    # Invoke renaming after metadata is available
    if media_files_metadata:
        rename_files(media_files_metadata)

    return None
