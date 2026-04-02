#!/bin/sh

if [ "$#" -eq 0 ]; then
  echo "Error: a test_name wasn't not provided"
  echo "Usage: ${0} test_name"

  exit 1
fi

python3 -m snakeviz profiling/$1.prof

exit 0
