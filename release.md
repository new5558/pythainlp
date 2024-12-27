# How to cut a new release

0. This project follows [semantic versioning][semver].
1. Ensure the version and release date fields (if any) in these files
   have been updated to the version of the new planned release:
    - `pyproject.toml`
    - `setup.cfg`
    - `setup.py`
    - `CITATION.cff`
    - `README.md`
    - `README.TH.md`
    - `CHANGELOG.md`
2. Navigate to the
  [releases page][releases] and
   click the "Draft a new release" button.
   Only project maintainers are able to perform this step.
3. Then enter the new tag in the "Choose a tag" box.
   The tag should begin with "v", as in, for instance, `v5.0.1`.
4. The release title should be the same as the new version tag.
   For instance, the title could be `v5.0.1`.
5. The click the "Generate release notes" button.
6. You can optionally include any particular thank-you's to contributors or
   reviewers in a note at the bottom of the release.
7. You can then click "publish release."
8. If the CI run is successful, then the release will be published on both
   the GitHub release page and also the [Python Package Index][pypi].

[semver]: https://semver.org/
[releases]: https://github.com/PyThaiNLP/pythainlp/releases
[pypi]: https://pypi.org/project/pythainlp/
