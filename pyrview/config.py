import jsonschema
import os
import yaml

module_path =  os.path.dirname(os.path.realpath(__file__))
project_path = os.path.abspath(module_path + os.sep + '..')

cfg_fn = project_path + '/etc/config.yaml'
schema_fn = project_path + '/etc/schemas/config-schema.yaml'

class Config(object):

    def __init__(self, cfg=cfg_fn, schema=schema_fn):

        # Load the schema and config yaml files
        self.schema = self.get_yaml_file(schema)
        self.document = self.get_yaml_file(cfg)

        # Validate the config to the schema
        try:
            jsonschema.validate(self.document, self.schema)
        except:
            raise

    def get_yaml_file(self, fn):
        try:
            with open(fn, 'r') as yamlfile:
                return yaml.load(yamlfile)
        except:
            raise
