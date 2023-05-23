#!/usr/bin/env python3

import unittest
import sys

if len(sys.argv) == 1:
    # Run all test files
    loader = unittest.TestLoader()
    suite = loader.discover('test', pattern='*_test.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
else:
    # Run specific test files
    for test_file in sys.argv[1:]:
        loader = unittest.TestLoader()
        suite = loader.discover('test', pattern=f'{test_file}_test.py')
        unittest.TextTestRunner(verbosity=2).run(suite)
