# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Spell checking and correction.
"""

__all__ = [
    "DEFAULT_SPELL_CHECKER",
    "NorvigSpellChecker",
    "correct",
    "correct_sent",
    "spell",
    "SENT_TOKS",
]

from pythainlp.spell.pn import NorvigSpellChecker

DEFAULT_SPELL_CHECKER = NorvigSpellChecker()

# these imports are placed here to avoid circular imports
from pythainlp.spell.core import correct, correct_sent, spell, SENT_TOKS
