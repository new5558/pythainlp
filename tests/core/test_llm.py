# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

import unittest

from pythainlp.llm import remove_repeated_ngrams


class LlmTestCase(unittest.TestCase):
    def test_remove_repeated_ngrams(self):
        texts = ['เอา', 'เอา', 'แบบ', 'แบบ', 'แบบ', 'ไหน']
        self.assertEqual(
            remove_repeated_ngrams(texts, n=1),
            ['เอา', 'แบบ', 'ไหน']
        )
        self.assertEqual(
            remove_repeated_ngrams(texts, n=2),
            ['เอา', 'เอา', 'แบบ', 'แบบ', 'ไหน']
        )
