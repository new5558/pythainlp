# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Unit test.

Each file in tests/ is for each main package.
"""

import sys
from unittest import TestLoader, TestSuite, TextTestRunner


def load_tests(loader: TestLoader, tests, pattern) -> TestSuite:
    suite = TestSuite()
    tests = loader.loadTestsFromName("tests.test_util.TestUtilPackage")
    suite.addTests(tests)
    tests = loader.loadTestsFromName("tests.test_tokenize.TestTokenizePackage")
    suite.addTests(tests)
    return suite
