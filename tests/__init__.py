# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Unit test.

Each file in tests/ is for each main package.
"""

import sys
from unittest import TestLoader, TestSuite, TextTestRunner


test_packages = [
    "tests.test_spell.TestSpellPackage",
    "tests.test_tokenize.TestTokenizePackage",
    "tests.test_util.TestUtilPackage",
]

def load_tests(loader: TestLoader, tests, pattern: str) -> TestSuite:
    """A function to load tests."""
    suite = TestSuite()
    for test_package in test_packages:
        tests = loader.loadTestsFromName(test_package)
        suite.addTests(tests)
    return suite
