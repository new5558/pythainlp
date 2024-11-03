# Test cases

Tests are categorized into three groups: core, compact, and extra.

## Core Tests (test_*.py)

- Focus on core functionalities.
- Do not rely on external dependencies beyond the standard library,
  except for `requests` which is used for corpus downloading.
- Test with all officially supported Python versions
  (currently 3.9, 3.10, 3.11, 3.12, and 3.13).

## Compact Tests (testc_*.py)

- Test a limited set of additional functionalities that rely on optional
  dependencies specified in `requirements.txt`.
- These dependencies are `PyYAML`, `numpy`, `pyicu`, `python-crfsuite`, and
  `requests`.
- Test with the latest two stable Python versions.

## Extra Tests (testx_*.py)

- Explore functionalities that rely on optional dependencies specified in the
  `extras` section of `setup.py`.
- These dependencies might include libraries like `gensim`, `nltk`, or `torch`.
- Due to dependency complexities, these functionalities are not part of the
  automated test suite and will not be tested in the CI/CD pipeline.

## Default Test Suite

The default test suite, executed by the `unittest tests` command, is defined
within `__init__.py` in this directory.
