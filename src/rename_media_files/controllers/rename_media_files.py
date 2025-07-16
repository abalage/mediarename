import os
from rename_media_files.config.config import AppArgs, datetime_format
from rename_media_files.utils.date_converter import DateConverter
from rename_media_files.models.media_files_model import MediaFilesModel
from rename_media_files.views.metadata_printer import MetadataPrinter
from rename_media_files.models.rename_media_files import rename_files


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
    input_path = args["input"]
    if isinstance(input_path, list):
        print("Error: input_path should be a string, not a list.")
        return

    files = get_files_from_input(input_path)
    media_files_model = MediaFilesModel(files)
    media_files_metadata = media_files_model.metadata

    if media_files_metadata and args.get("verbose", False):
        metadata_printer = MetadataPrinter(media_files_metadata)
        metadata_printer.print_metadata_list()

    # Invoke renaming after metadata is available
    if media_files_metadata:
        rename_files(media_files_metadata, args.get("target_dir"))

    return None