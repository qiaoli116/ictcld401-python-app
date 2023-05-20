#!/bin/bash

# Check if any test file arguments are provided
if [ $# -eq 0 ]; then
  # Run all test files
  python3 -m unittest discover -s test -p "*_test.py" -v
else
  # Run specific test files
  for test_file in "$@"; do
    python3 -m unittest discover -s test -p "${test_file}_test.py" -v
  done
fi