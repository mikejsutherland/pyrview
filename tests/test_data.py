import json
import os
import unittest
import context

from pyrview.config import Config

from pyrview.data.file import File
from pyrview.data.nagios_api import NagiosAPI

path = os.path.dirname(os.path.realpath(__file__));

class TestFile(unittest.TestCase):

    def setUp(self):
        self.document = {
            "data": {
                "source": path + "/data/data.json",
                "type": "file"
            }
        }
        self.file = File(self.document)
        data = self.file.load()

    def test_load(self):
        self.assertTrue(self.file.data)
        self.assertIsInstance(self.file.data, list, "data is list type")
        self.assertEqual(self.file.index, 0, "node index is 0")
        self.assertEqual(self.file.size, 3, "data size is 3")

    def test_get(self):
        node = self.file.get()
        self.assertTrue(node)
        self.assertIsInstance(node, dict, "node is dict type")
        self.assertEqual(self.file.index, 0, "node index is 0")
        self.assertEqual(self.file.size, 3, "data size is 3")

    def test_next(self):
        next_node = self.file.get()
        for idx, node in enumerate(self.file.data):
            self.assertIsInstance(next_node, dict, "data is list type")
            self.assertEqual(node, next_node)
            self.assertEqual(self.file.index, idx, "node index is "+ str(idx))
            next_node = self.file.next()

    def test_prev(self):
        prev_node = self.file.prev()
        for node in reversed(self.file.data):
            idx = self.file.data.index(node)
            self.assertIsInstance(prev_node, dict, "data is list type")
            self.assertEqual(node, prev_node)
            self.assertEqual(self.file.index, idx, "node index is "+ str(idx))
            prev_node = self.file.prev()


class TestNagiosAPI(unittest.TestCase):

    def setUp(self):
        config = Config(path + "/etc/config.yaml")
        self.document = config.document
        self.nagios_api = NagiosAPI(self.document)

        try:
            with open(path + "/data/nagios_api.json", "r") as jsonfile:
                data = json.load(jsonfile)
        except:
            raise
        data = self.nagios_api.load(data)

        #self.nagios_api.transform(data)
        #self.nagios_api.reindex(len(self.nagios_api.data))

    def test_document(self):
        self.assertTrue(self.document)
        self.assertIsInstance(self.document, dict, "document is dict type")

    def test_load(self):
        self.assertTrue(self.nagios_api.data)
        self.assertIsInstance(self.nagios_api.data, list, "data is list type")
        self.assertEqual(self.nagios_api.index, 0, "node index is 0")
        self.assertEqual(self.nagios_api.size, 5, "data size is 5")

    def test_get(self):
        node = self.nagios_api.get()
        self.assertTrue(node)
        self.assertIsInstance(node, dict, "node is dict type")
        self.assertEqual(self.nagios_api.index, 0, "node index is 0")
        self.assertEqual(self.nagios_api.size, 5, "data size is 5")

    def test_next(self):
        next_node = self.nagios_api.get()
        for idx, node in enumerate(self.nagios_api.data):
            self.assertIsInstance(next_node, dict, "data is list type")
            self.assertEqual(node, next_node)
            self.assertEqual(self.nagios_api.index, idx, "node index is "+ str(idx))
            next_node = self.nagios_api.next()

    def test_prev(self):
        prev_node = self.nagios_api.prev()
        for node in reversed(self.nagios_api.data):
            idx = self.nagios_api.data.index(node)
            self.assertIsInstance(prev_node, dict, "data is list type")
            self.assertEqual(node, prev_node)
            self.assertEqual(self.nagios_api.index, idx, "node index is "+ str(idx))
            prev_node = self.nagios_api.prev()

if __name__ == '__main__':
    unittest.main()
