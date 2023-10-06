import wx
from .lang_const import SUPPORTED_LANG
from kicad_amf_plugin.utils.images import Smiles
class LangSettingPopMenu(wx.Menu):
    def __init__(self , current_lang_id  : int):
        super().__init__()
        for idx ,lang in enumerate(SUPPORTED_LANG):
            item = wx.MenuItem(self,  idx, SUPPORTED_LANG[lang] )
            if current_lang_id == lang :
                item.SetBitmap(Smiles.GetBitmap())
            self.Append(item)

