import json
import os

from pyrview.data.core import Data

module_path =  os.path.dirname(os.path.realpath(__file__))
project_path = os.path.abspath(module_path + os.sep + '../..')

schema_fn = project_path + '/etc/schemas/file-schema.yaml'

class File(Data):

    def __init__(self, document, schema=schema_fn):
        self.schema = self.get_yaml_file(schema)
        super().__init__(document)

    def load(self):
        self.reindex()
        try:
            with open(self.source) as data_file:
                self.data = json.load(data_file)
        except:
            raise

        # Validate the data retrieved with the schema
        self.validate()

        # Reindex and return data
        self.reindex(len(self.data));

        return self.data
