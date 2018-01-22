import json
import os
import urllib.request

from pyrview.data.core import Data

module_path =  os.path.dirname(os.path.realpath(__file__))
project_path = os.path.abspath(module_path + os.sep + '../..')

file_schema_fn = project_path + '/etc/schemas/file-schema.yaml'
nagios_schema_fn = project_path + '/etc/schemas/nagios-api-schema.yaml'

class NagiosAPI(Data):

    def __init__(self, document, file_schema=file_schema_fn, nagios_schema=nagios_schema_fn):
        self.file_schema = self.get_yaml_file(file_schema)
        self.nagios_schema = self.get_yaml_file(nagios_schema)
        super().__init__(document)

    def load(self, data=None):
        self.reindex()

        if data is None:
            try:
                resp = urllib.request.urlopen(self.source).read()
                data = json.loads(resp.decode('utf-8'))
            except:
                raise

        # Validate nagios-api data
        self.validate(data, self.nagios_schema)

        # Transform the nagios data into the file format
        self.transform(data)

        # Validate the data retrieved with the schema
        self.validate(self.data, self.file_schema)

        # Reindex and return data
        self.reindex(len(self.data));

        return self.data

    def transform(self, response):
        self.data = []

        for sysname in response['content']:
            resources = []
            services = response['content'][sysname]['services']

            for resname in services:
                services[resname]['name'] = resname
                services[resname]['value'] = services[resname]['plugin_output']
                services[resname]['status'] = int(services[resname]['current_state'])

                resources.append(services[resname])

            self.data.append({
                "name": sysname,
                "status": "",
                "resources": resources
            })
