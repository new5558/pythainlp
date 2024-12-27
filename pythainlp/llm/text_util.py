# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
# ruff: noqa: C901

from typing import List


def remove_repeated_ngrams(string_list: List[str], n: int = 2) -> List[str]:
    """
    Remove repeated n-grams

    :param List[str] string_list: List of string
    :param int n: n-gram size
    :return: List of string
    :rtype: List[str]

    :Example:
    ::

        from pythainlp.llm import remove_repeated_ngrams

        remove_repeated_ngrams(['เอา', 'เอา', 'แบบ', 'ไหน'], n=1)
        # output: ['เอา', 'แบบ', 'ไหน']
    """
    if not string_list or n <= 0:
        return string_list

    unique_ngrams = set()

    output_list = []

    for i in range(len(string_list)):
        if i + n <= len(string_list):
            ngram = tuple(string_list[i:i + n])

            if ngram not in unique_ngrams:
                unique_ngrams.add(ngram)

                if not output_list or output_list[-(n - 1):] != list(ngram[:-1]):
                    output_list.extend(ngram)
                else:
                    output_list.append(ngram[-1])
        else:
            for char in string_list[i:]:
                if not output_list or output_list[-1] != char:
                    output_list.append(char)

    return output_list
