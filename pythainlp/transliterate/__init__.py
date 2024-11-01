# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Transliteration.
"""

__all__ = [
    "pronunciate",
    "puan",
    "romanize",
    "transliterate",
]

from pythainlp.transliterate.core import pronunciate, romanize, transliterate
from pythainlp.transliterate.spoonerism import puan
