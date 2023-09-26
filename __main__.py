import sys
from kicad_amf_plugin.gui.app_base import BaseApp
from kicad_amf_plugin.gui.main_dialog import MainWindow

if __name__ == '__main__':
    app = BaseApp(redirect=False)
    frame = MainWindow(None)
    frame.Show()
    sys.exit(app.MainLoop())
