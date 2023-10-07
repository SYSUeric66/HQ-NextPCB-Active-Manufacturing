# -*- coding: utf-8 -*-
#
# Author:  Werner F. Bruhin
# Purpose: Application constants
# Created: 06/04/2012

import wx
_=wx.GetTranslation

# language domain
LANG_DOMAIN = "kicad_amf_plugin"
# languages you want to support
SUPPORTED_LANG = { wx.LANGUAGE_ENGLISH : _("en"),
                wx.LANGUAGE_JAPANESE_JAPAN :    _("ja"),
                wx.LANGUAGE_CHINESE_SIMPLIFIED :  _("zh_CN")
                }
