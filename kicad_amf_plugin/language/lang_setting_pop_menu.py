import wx
from .lang_const import SUPPORTED_LANG
from kicad_amf_plugin.utils.images import Smiles
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER

class LangSettingPopMenu(wx.Menu):
    def __init__(self , current_lang_id  : int):
        super().__init__()
        for _ ,lang in enumerate(SUPPORTED_LANG):
            item = wx.MenuItem(self,  lang, SUPPORTED_LANG[lang] )
            if current_lang_id == lang :
                item.SetBitmap(Smiles.GetBitmap())
            self.Append(item)
            if wx.LANGUAGE_ENGLISH == lang :
                self.Bind(wx.EVT_MENU , self.setup_en, id= lang )
            elif  wx.LANGUAGE_JAPANESE == lang :
                self.Bind(wx.EVT_MENU , self.setup_jp, id= lang )
            elif  wx.LANGUAGE_CHINESE_SIMPLIFIED == lang :
                self.Bind(wx.EVT_MENU , self.setup_zh, id= lang )

    def setup_en(self ,evt):
        SETTING_MANAGER.set_language(wx.LANGUAGE_ENGLISH)

    def setup_jp(self ,evt):
        SETTING_MANAGER.set_language(wx.LANGUAGE_JAPANESE)

    def setup_zh(self , evt):
        SETTING_MANAGER.set_language(wx.LANGUAGE_CHINESE_SIMPLIFIED)                


