#!/bin/bash

# Check if any test file arguments are provided
if [ $# -eq 0 ]; then
  # Run all test files
  python -m unittest discover -s test -p "*_test.py" -f -v
else
  # Run specific test files
  for test_file in "$@"; do
    python -m unittest discover -s test -p "${test_file}_test.py" -f -v
  done
fi