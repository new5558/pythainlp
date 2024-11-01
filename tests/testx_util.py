# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0

"""
Unit tests for pythainlp.util module.
"""

import unittest

from pythainlp.util import rhyme, thai_word_tone_detector
from pythainlp.util.spell_words import spell_word


class UtilTestCaseX(unittest.TestCase):
    def testx_rhyme(self):
        self.assertIsInstance(rhyme("แมว"), list)
        self.assertTrue(len(rhyme("แมว")) > 2)

    def test_spell_word(self):
        self.assertEqual(spell_word("เสือ"), ["สอ", "เอือ", "เสือ"])
        self.assertEqual(spell_word("เสื้อ"), ["สอ", "เอือ", "ไม้โท", "เสื้อ"])
        self.assertEqual(spell_word("คน"), ["คอ", "นอ", "คน"])
        self.assertEqual(
            spell_word("คนดี"), ["คอ", "นอ", "คน", "ดอ", "อี", "ดี", "คนดี"]
        )

    def testx_thai_word_tone_detector(self):
        self.assertIsNotNone(thai_word_tone_detector("คนดี"))
        self.assertEqual(
            thai_word_tone_detector("ราคา"), [("รา", "m"), ("คา", "m")]
        )
