def _main():
        import sys
        from kicad_amf_plugin.gui.app_base import BaseApp
        from kicad_amf_plugin.gui.main_dialog import MainWindow
        app = BaseApp(redirect=False)
        frame = MainWindow(None)
        frame.ShowModal()
        app.MainLoop()
