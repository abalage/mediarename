'''
The configuration is coming from two directions:
1. arguments passed to the main method (AppArgs object)
2. read from a configuration file (AppConfig object).
'''
from typing import TypedDict, List, Dict
from pydantic import BaseModel, ValidationError, Field
from gettext import gettext as _


class AppArgs(TypedDict):
    verbose: bool
    input: List[str]

class FileMetadata(BaseModel):
    file_path: str
    creation_date: str = Field(..., description="Creation date in the format YYYY-MM-DD")
    modification_date: str = Field(..., description="Modification date in the format YYYY-MM-DD")
    file_type: str = Field(..., description="Type of the file (e.g., image, video, audio)")
    mime_type: str = Field(..., description="File format (e.g., jpg, mp4, mp3)")

datetime_format = '%Y%m%d_%H%M%S'
