"""
Content models
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ContentValue:
    """
    Content Value Dataclass
    """
    value: str
    count: int = None
