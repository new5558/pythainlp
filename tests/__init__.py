# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Unit test.

Each file in tests/ is for each main package.
"""

from unittest import TestLoader, TestSuite

test_packages: list[str] = [
    # "tests.test_ancient",
    # "tests.test_cli",
    # "tests.test_corpus",
    # "tests.test_soundex",
    # "tests.test_spell",
    "tests.test_tokenize",
    # "tests.test_transliterate",
    # "tests.test_util",
]


def load_tests(
    loader: TestLoader, standard_tests: TestSuite, pattern: str
) -> TestSuite:
    """Load test protocol"""
    suite = TestSuite()
    for test_package in test_packages:
        tests = loader.loadTestsFromName(test_package)
        suite.addTests(tests)
    return suite
