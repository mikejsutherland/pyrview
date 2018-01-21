import sys
sys.dont_write_bytecode = True

import os
import unittest
import context

test_path = os.path.dirname(os.path.realpath(__file__))

test_loader = unittest.TestLoader()
tests = test_loader.discover(test_path, 'test_*.py')
test_runner = unittest.runner.TextTestRunner()
test_runner.run(tests)
