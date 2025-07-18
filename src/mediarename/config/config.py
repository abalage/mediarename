from typing import TypedDict
from pydantic import BaseModel, Field


class AppArgs(TypedDict):
    """
    TypedDict for application arguments.

    Attributes:
        verbose (bool): Flag to enable verbose output.
        input (str): Path to input file or directory.
    """
    verbose: bool
    input: str
    datetime_format: str
    dry_run: bool


class FileMetadata(BaseModel):
    """
    Model representing metadata for a media file.

    Attributes:
        file_path (str): Path to the media file.
        creation_date (str): Creation date in the format YYYY-MM-DD.
        modification_date (str): Modification date in the format YYYY-MM-DD.
        file_type (str): Type of the file (e.g., image, video, audio).
        mime_type (str): File format (e.g., jpg, mp4, mp3).
    """
    file_path: str
    creation_date: str = Field(..., description="Creation date in the format YYYY-MM-DD")
    modification_date: str = Field(..., description="Modification date in the format YYYY-MM-DD")
    file_type: str = Field(..., description="Type of the file (e.g., image, video, audio)")
    mime_type: str = Field(..., description="File format (e.g., jpg, mp4, mp3)")
