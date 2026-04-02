#!/bin/bash

if ["$#" -eq 0]; then
  echo "Error: provide a test_route and test_name weren't provided"
  echo "Usage: ${0} test_route test_name"

  exit 1
fi

python3 -m memory_profiler pytest -s -vv tests/$1.py -k "${2}"

exit 0
