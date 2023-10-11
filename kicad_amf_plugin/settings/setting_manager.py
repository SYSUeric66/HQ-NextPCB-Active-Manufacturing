
import wx
import os
from kicad_amf_plugin.gui.event.pcb_fabrication_evt_list import LocaleChangeEvent
from .kicad_setting import KiCadSetting
APP_NAME = 'kicad_amf_plugin'

VENDOR_NAME = 'NextPCB'

LANGUAGE = 'language'


ORDER_REGION = "order_region"
AVAILABLE_REGIONS = [ _(u"CN"), _(u"JP"), _(u"EU/USA") ]

PRICE_UNIT = {
    0 : '¥',
    1 : '$'
}


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
            self.set_language(KiCadSetting.read_lang_setting())
            self.app_conf.Flush()

    def register_app(self, app : wx.App):
        self.app = app            

    def set_language( self, now : int ):
        old = self.language
        if old == now:
            return                    
        self.app_conf.WriteInt(key=LANGUAGE, value=now)
        if self.app:
            evt = LocaleChangeEvent(id = -1)
            evt.SetInt(now)
            self.app_conf.Flush()
            wx.PostEvent(self.app ,evt)

    @property
    def language(self):
        return self.app_conf.ReadInt(LANGUAGE)
    

    def set_order_region(self , region : int):
        self.app_conf.WriteInt(key=ORDER_REGION, value=region)

    @property
    def order_region(self):
        return self.app_conf.ReadInt(ORDER_REGION)

    def get_price_unit(self):
        return PRICE_UNIT[0] if not self.order_region  else PRICE_UNIT[1]


SETTING_MANAGER = _SettingManager()
