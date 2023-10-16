#! /bin/python
import os
import sys

PLUGIN_ROOT =os.path.dirname(os.path.abspath(__file__))
if PLUGIN_ROOT not in sys.path:
    sys.path.append(PLUGIN_ROOT)


class KicadPluginBuilder:

    def update_plugin_version(self):
        pass    
    
    def update_translation(self):
        pass

    
    def create_plugins_dir(self):
        pass

    def cp_resource_dir(self):
        pass

    def create_zip_file(self):
        pass

    def write_metadata_json(self) :
        pass


if __name__ == '__main__':
    builder = KicadPluginBuilder()
    builder.update_plugin_version()
    builder.update_translation()
    builder.create_plugins_dir()
    builder.cp_resource_dir()
    builder.write_metadata_json()
    builder.create_zip_file()