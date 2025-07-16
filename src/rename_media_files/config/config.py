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
