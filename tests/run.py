import sys
import os
import unittest

sys.dont_write_bytecode = True
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(path + os.sep + '..'))

test_path = os.path.dirname(os.path.realpath(__file__))

test_loader = unittest.TestLoader()
tests = test_loader.discover(test_path, 'test_*.py')
test_runner = unittest.runner.TextTestRunner()
test_runner.run(tests)
