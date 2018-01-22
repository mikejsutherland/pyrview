import jsonschema
import yaml

class Data(object):

    def __init__(self, document):
        if document:
            self.source = document['data']['source']
            self.type = document['data']['type']
        else:
            raise ValueError('Missing or undefined config document')

        self.data = dict()
        self.size = 0
        self.index = 0

    def load(self):
        pass

    def reindex(self, size=0, index=0):
        self.size = size
        self.index = index

    def get(self):
        if self.data:
            if self.data[self.index]:
                return self.data[self.index]
            else:
                self.reindex(len(self.data))
                return self.data[self.index]
        else:
            return None

    def next(self):
        self.index += 1

        if self.index >= self.size:
            self.index = 0

        return self.get()

    def prev(self):
        self.index -= 1

        if self.index < 0:
            self.index = ( self.size - 1 )

        return self.get()

    def validate(self, data=None, schema=None):
        if data is None:
            data = self.data

        if schema is None:
            schema = self.schema

        try:
            jsonschema.validate(data, schema)
        except:
            raise

    def get_yaml_file(self, fn):
        try:
            with open(fn, 'r') as yamlfile:
                return yaml.load(yamlfile)
        except:
            raise
