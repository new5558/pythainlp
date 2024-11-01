# Test cases

Tests are categorized into two groups: fundamental and extra.

## Fundamental Tests (test_*.py)

- Focus on core functionalities.
- Do not rely on additional dependencies beyond those listed in the
  `requirements` section of `setup.py`.

## Extra Tests (testx_*.py)

- Explore functionalities that rely on optional dependencies specified in the
  `extras` section of `setup.py`.
- These dependencies might include libraries like `nltk`, `pycrfsuite`, or
  `torch`.

## Default Test Suite

The default test suite, executed by the `unittest tests` command, is defined
within `__init__.py` in this directory.
