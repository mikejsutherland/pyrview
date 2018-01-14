from jsonschema import validate
import yaml
import os

class Load(object):

    def __init__(self, cfg='etc/config.yaml'):
        path = os.path.dirname(os.path.realpath(__file__))
        self.dir = os.path.abspath(path + os.sep + '..')
        self.cfg_path = self.dir + os.sep + cfg
        self.schema_path = self.dir + os.sep + 'etc/config-schema.yaml'
        # Load the schema and config yaml files
        self.schema = self._load_yaml_document(self.schema_path)
        self.document = self._load_yaml_document(self.cfg_path)
        # Validate the config to the schema
        self._validate_document()

    def _load_yaml_document(self, fn):
        try:
            with open(fn, 'r') as yamlfile:
                return yaml.load(yamlfile)
        except:
            raise

    def _validate_document(self):
        try:
            validate(self.document, self.schema)
        except:
            raise
