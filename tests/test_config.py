import unittest
import context
import os

from pyrview.config import Config

path = os.path.dirname(os.path.realpath(__file__));

class LoadConfig(unittest.TestCase):

    def setUp(self):
        self.config = Config(path + "/etc/config.yaml")
        self.document = self.config.document

    def test_document(self):
        self.assertTrue(self.document)
        self.assertIsInstance(self.document, dict, "document is dict type")


if __name__ == '__main__':
    unittest.main()
