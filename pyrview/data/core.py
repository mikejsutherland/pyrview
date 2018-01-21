import jsonschema

class Data(object):

    def __init__(self, document):
        if document:
            self.source = document['data']['source']
            self.type = document['data']['type']
        else:
            raise ValueError('Missing or undefined config document')

    def validate(self):
        try:
            jsonschema.validate(self.data, self.schema)
        except:
            raise

    def get(self):
        pass

    def next(self):
        pass

    def prev(self):
        pass
