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
    "spell_sent",
]

from pythainlp.spell.core import correct, correct_sent, spell, spell_sent

DEFAULT_SPELL_CHECKER = NorvigSpellChecker()

from pythainlp.spell.pn import NorvigSpellChecker
