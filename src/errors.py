"""
errors.py

Module for creating detailed error
messages for specific use within
this software
"""

from __future__ import annotations


class KanaKingException(Exception):
    """
    General exception for problems within the
    application
    """


class TransliterationError(KanaKingException):
    """
    Used to indicate that a certain syllable
    cannot be transliterated.
    """
