"""Console script for rename-media-files."""
import argparse
from mediarename.controllers.mediarename import main as process
from mediarename.config.config import AppArgs


def parse_arguments() -> AppArgs:
    # Set up argument parser
    parser = argparse.ArgumentParser(description="A package to mass rename media files based on their metadata. Falls back to the file creation date if metadata is not available.")  # noqa: E501
    parser.add_argument('input', type=str, help='Input to read. File or directory.')
    parser.add_argument('--datetime-format', '-d', type=str, default='%Y%m%d_%H%M%S',
                        help='Format for datetime strings used in renaming. Default: "%%Y%%m%%d_%%H%%M%%S". Check the manual of date for possible formats.')  # noqa: E501
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Do not rename anything, just show the list of files to be renamed with their new names.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs.')
    parser.add_argument('--version', action='version', version='Rename Media Files', help='Show the version of the program.')  # noqa: E501

    # Parse the arguments
    parsed_args = parser.parse_args()

    args: AppArgs = {
        'input': parsed_args.input,
        'datetime_format': parsed_args.datetime_format,
        'dry_run': parsed_args.dry_run,
        'verbose': parsed_args.verbose
    }
    return args


def main_cli() -> None:
    args: AppArgs = parse_arguments()
    process(args)


if __name__ == "__main__":
    main_cli()
