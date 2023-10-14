"""
Context models
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Context:
    """
    Context dataclass
    """
    keys: list = None
    items: dict = None
    values: list = None
    types: dict = None
