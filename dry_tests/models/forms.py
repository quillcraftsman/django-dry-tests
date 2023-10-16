"""
Form models
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Fields:
    """
    TrueForm Fields
    """
    count: int = None
    names: list = None
    types: dict = None


@dataclass(frozen=True)
class TrueForm:
    """
    True form class to use in asserts
    """
    fields: Fields | dict = None
