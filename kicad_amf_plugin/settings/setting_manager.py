import json

import wx
import os
import logging
from kicad_amf_plugin.gui.event.locale_change_evt import LocaleChangeEvent

APP_NAME = 'kicad_amf_plugin'

VENDOR_NAME = 'NextPCB'

LANGUAGE = 'language'


def read_kicad_lang_setting():
    try:
        import pcbnew
        kicad_setting_path = str(pcbnew.SETTINGS_MANAGER.GetUserSettingsPath())
        logging.info(f'Kicad setting path {kicad_setting_path}')
        print(f'Kicad setting path {kicad_setting_path}')
        if len(kicad_setting_path):
            kicad_common_json = os.path.join(kicad_setting_path, 'kicad_common.json')
            with open(kicad_common_json) as f :
                data = json.loads(f.read())
                lang : str = data["system"]["language"]
                if lang.count("中文"):
                    return wx.LANGUAGE_CHINESE_SIMPLIFIED
                elif lang.count("日本"):
                    return wx.LANGUAGE_JAPANESE
        else:
            logging.error("Empty KiCad config path!")
    except:
        logging.error("Cannot read the language setting of KiCad!")
    return wx.LANGUAGE_ENGLISH

class _SettingManager(wx.EvtHandler) :
    def __init__(self) -> None:
        self.app : wx.App = None
        sp = wx.StandardPaths.Get()
        config_loc = sp.GetUserConfigDir()
        config_loc = os.path.join(config_loc, APP_NAME)

        if not os.path.exists(config_loc):
            os.mkdir(config_loc)

        self.app_conf = wx.FileConfig(appName=APP_NAME,
                                       vendorName=VENDOR_NAME,
                                       localFilename=os.path.join(
                                           config_loc, "common.ini"))

        if not self.app_conf.HasEntry(LANGUAGE):
            self.set_language(read_kicad_lang_setting())
        self.app_conf.Flush()

    def set_language( self, now : int ):
        old = self.language
        self.app_conf.WriteInt(key=LANGUAGE, value=now)
        if self.app and old != now:
            evt = LocaleChangeEvent(id = -1)
            evt.SetInt(now)
            wx.PostEvent(self.app ,evt)

    @property
    def language(self):
        return self.app_conf.ReadInt(LANGUAGE)

    def register_app(self, app : wx.App):
        self.app = app


SETTING_MANAGER = _SettingManager()
