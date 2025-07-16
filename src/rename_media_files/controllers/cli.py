"""Console script for rename-media-files."""
import argparse
from rename_media_files.controllers.rename_media_files import main as process
from rename_media_files.config.config import AppArgs


def parse_arguments() -> AppArgs:
    # Set up argument parser
    parser = argparse.ArgumentParser(description="A package to mass rename media files based on their metadata.")
    parser.add_argument('input', type=str, help='Input to read. File or directory.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print categorized rows for troubleshooting.')
    parser.add_argument('--version', action='version', version='Rename Media Files', help='Show the version of the program.')  # noqa: E501

    # Parse the arguments
    parsed_args = parser.parse_args()

    args: AppArgs = {
        'input': parsed_args.input,
        'verbose': parsed_args.verbose
    }
    return args


def main_cli() -> None:
    args = parse_arguments()
    df = process(args)
    print(df)


if __name__ == "__main__":
    main_cli()
