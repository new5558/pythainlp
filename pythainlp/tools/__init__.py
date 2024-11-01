# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
__all__ = [
    "PYTHAINLP_DEFAULT_DATA_DIR",
    "get_full_data_path",
    "get_pythainlp_data_path",
    "get_pythainlp_path",
    "warn_deprecation",
]

from pythainlp.tools.core import warn_deprecation
from pythainlp.tools.path import (
    PYTHAINLP_DEFAULT_DATA_DIR,
    get_full_data_path,
    get_pythainlp_data_path,
    get_pythainlp_path,
)
