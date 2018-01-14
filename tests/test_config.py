import unittest

from pyrview import config

class LoadConfig(unittest.TestCase):

    def setUp(self):
        self.config = config.Load()
        self.document = self.config.document

    def test_document(self):
        self.assertTrue(self.document)
        self.assertIsInstance(self.document, dict, "document is dict type")


if __name__ == '__main__':
    unittest.main()
