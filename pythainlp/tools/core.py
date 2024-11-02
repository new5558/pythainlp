# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
Generic support functions for PyThaiNLP.
"""

import sys
import warnings


def warn_deprecation(
    deprecated_func: str,
    replacing_func: str = "",
    version: str = "",
):
    """Warn about the deprecation of a function.

    :param str deprecated_func: Name of the deprecated function.
    :param str replacing_func: Name of the function to use instead (optional).
    :param str version: PyThaiNLP version in which the function will be deprecated (optional).
    """
    if version:
        version = f"PyThaiNLP {version}"
    else:
        version = "a future release"
    message = f"The '{deprecated_func}' function is deprecated and will be removed in {version}."
    if replacing_func:
        message += f" Please use '{replacing_func}' instead."
    warnings.warn(message, DeprecationWarning, stacklevel=2)


def safe_print(text: str):
    """Print text to console, handling UnicodeEncodeError.

    :param text: Text to print.
    :type text: str
    """
    try:
        print(text)
    except UnicodeEncodeError:
        print(
            text.encode(sys.stdout.encoding, errors="replace").decode(
                sys.stdout.encoding
            )
        )
