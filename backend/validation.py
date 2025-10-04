from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field

#classification of the severity
class Severity(IntEnum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW =4

class