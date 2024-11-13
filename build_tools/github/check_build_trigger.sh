#!/bin/bash

set -e
set -x

COMMIT_MSG=$(git log --no-merges -1 --oneline)

# The commit marker "[cd build]" will trigger the build when required
if [[ "$GITHUB_EVENT_NAME" == "workflow_dispatch" ||
      "$GITHUB_EVENT_NAME" == "release" ||
      "$COMMIT_MSG" =~ "[cd build]" ]]; then
    echo "build=true" >> $GITHUB_OUTPUT
fi
