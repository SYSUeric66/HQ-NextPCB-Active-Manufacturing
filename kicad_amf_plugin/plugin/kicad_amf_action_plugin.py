import sys
import pcbnew
import os

class KiCadAmfActionPlugin(pcbnew.ActionPlugin):
    def __init__(self):
        self.name = "HQ NextPCB Active Manufacturing"
        self.category = "Manufacturing"
        self.description = "Quote and place order with one button click."
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(
           os.path.dirname(__file__),'icon.png')
        self.dark_icon_file_name = os.path.join(
            os.path.dirname(__file__),  'icon.png')

    def Run(self):
        PLUGIN_ROOT =os.path.abspath(os.path.join( os.path.abspath(os.path.dirname(os.path.abspath(__file__))  ) ,'..' ,'..' ))
        sys.path.append(PLUGIN_ROOT)
        from kicad_amf_plugin.plugin._main import _main
        _main()