"""
readings.py

Used to convert between romanized Japanese
(romaji) and Japanese kana.

NOTE: This software currently only supports
the Waapuro-Romaji system, which is the
standard for text entry and is the most
straighforward to implement.
"""

# pylint: disable=import-error
# pylint: disable=unused-import


from __future__ import annotations

from config.constants import (
    ROMAJI_TO_HIRAGANA,
    HIRAGANA_TO_ROMAJI,
    ROMAJI_TO_KATAKANA,
    KATAKANA_TO_ROMAJI

)

from errors import TransliterationError


def convert_h_to_r(hiragana: str) -> str:
    """
    Transliterates a given hiragana
    string into the romanized version
    """

    romanized = ""

    index = 0

    # Parse through the entire string
    while index < len(hiragana):
        # 2-letter syllable
        if hiragana[index:index+2] in HIRAGANA_TO_ROMAJI.keys():
            romanized += HIRAGANA_TO_ROMAJI[hiragana[index:index+2]]
            index += 2

        # 1-letter syllable
        elif hiragana[index] in HIRAGANA_TO_ROMAJI.keys():
            romanized += HIRAGANA_TO_ROMAJI[hiragana[index]]
            index += 1

        # Small tsu
        elif hiragana[index] == "っ":
            if hiragana[index+1] in "かきくけこさしすせそたちつてとぱぴぷぺぽ":
                # Small tsu doubles the next sound
                romanized += HIRAGANA_TO_ROMAJI[hiragana[index+1]][0]
                index += 1
            else:
                raise TransliterationError(
                        f"Invalid combination: Cannot place 'っ' before '{hiragana[index+1]} in word {hiragana}'"
                    )

        else:
            raise TransliterationError(f"Failed to transliterate '{hiragana}' at char {index}")

    return romanized

def convert_r_to_h(romaji: str) -> str:
    """
    Converts romanized Japanese to into the original hiragana
    """
    hiragana = ""
    index = 0

    # Parse through entire string
    while index < len(romaji):
        # 3-letter syllables
        if romaji[index:index+3] in ROMAJI_TO_HIRAGANA.keys():
            hiragana += ROMAJI_TO_HIRAGANA[romaji[index:index+3]]
            index += 3

        # 2-letter syllables
        elif romaji[index:index+2] in ROMAJI_TO_HIRAGANA.keys():
            hiragana += ROMAJI_TO_HIRAGANA[romaji[index:index+2]]
            index += 2

        # 1-letter syllables
        elif romaji[index] in ROMAJI_TO_HIRAGANA.keys():
            hiragana += ROMAJI_TO_HIRAGANA[romaji[index]]
            index += 1

        # Doubled consonants (e.g. kka, tto, sshi)
        elif romaji[index] == romaji[index+1]:
            if romaji[index] in "kstp":
                hiragana += "っ"
                index += 1
            else:
                raise TransliterationError(
                    f"Invalid combination: Cannot double {romaji[index]*2} in {romaji}"
                )
        else:
            raise TransliterationError(
                f"Failed to transliterate '{romaji}' at char {index}"
                )

    return hiragana


def convert_k_to_r(katakana: str) -> str:
    """
    Transliterates a given katakana
    string into the romanized version
    """
    romanized = ""

    index = 0

    # Parse through the entire string
    while index < len(katakana):
        # 2-letter syllable
        if katakana[index:index+2] in KATAKANA_TO_ROMAJI.keys():
            romanized += KATAKANA_TO_ROMAJI[katakana[index:index+2]]
            index += 2

        # 1-letter syllable
        elif katakana[index] in KATAKANA_TO_ROMAJI.keys():
            romanized += KATAKANA_TO_ROMAJI[katakana[index]]
            index += 1

        # Small tsu
        elif katakana[index] == "ッ":
            if katakana[index+1] in "カキクケコサシスセソタチツテトパピプペポ":
                # Small tsu doubles the next sound
                romanized += KATAKANA_TO_ROMAJI[katakana[index+1]][0]
                index += 1
            else:
                raise TransliterationError(
                        f"Invalid combination: Cannot place 'ッ' before '{katakana[index+1]} in word {katakana}'"
                    )
        elif katakana[index] == "ー":
            if index > 0:
                if katakana[index-1] != "ン":
                    romanized += romanized[-1]
                    index += 1
                else:
                    raise TransliterationError(
                        "Cannot place 'ー' after 'ン'. No vowel to double!"
                    )

            else:
                raise TransliterationError(
                    "'ー' cannot be the first character in a word."
                )

        else:
            raise TransliterationError(f"Failed to transliterate '{katakana}' at char {index}")

    return romanized

def convert_r_to_k(romaji: str) -> str:
    """
    Converts romanized Japanese to into the original katakana
    """
    katakana = ""
    index = 0

    # Parse through entire string
    while index < len(romaji):

        # Doubled letter
        if romaji[index] in "aeiou" and romaji[index] == romaji[index-1]:
            katakana += "ー"
            index += 1

        # 3-letter syllables
        elif romaji[index:index+3] in ROMAJI_TO_KATAKANA.keys():
            katakana += ROMAJI_TO_KATAKANA[romaji[index:index+3]]
            index += 3

        # 2-letter syllables
        elif romaji[index:index+2] in ROMAJI_TO_KATAKANA.keys():
            katakana += ROMAJI_TO_KATAKANA[romaji[index:index+2]]
            index += 2

        # 1-letter syllables
        elif romaji[index] in ROMAJI_TO_KATAKANA.keys():
            katakana += ROMAJI_TO_KATAKANA[romaji[index]]
            index += 1

        # Doubled consonants (e.g. kka, tto, sshi)
        elif romaji[index] == romaji[index+1]:
            if romaji[index] in "kstp":
                katakana += "ッ"
                index += 1
            else:
                raise TransliterationError(
                    f"Invalid combination: Cannot double {romaji[index]*2} in {romaji}"
                )
        else:
            raise TransliterationError(
                f"Failed to transliterate '{romaji}' at char {index}"
                )

    return katakana
