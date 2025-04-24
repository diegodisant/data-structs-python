#!/bin/sh

if [ "$#" -eq 0 ]; then
  echo 'Error: a test_name wasnt provided please use as follows'
  echo "${0} test_name"

  exit 1
fi

python3 -m snakeviz $1

exit 0
