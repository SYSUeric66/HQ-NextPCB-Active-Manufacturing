# -*- coding: utf-8 -*-
#
# Author:  Werner F. Bruhin
# Purpose: Application constants
# Created: 06/04/2012

import wx
_=wx.GetTranslation

# language domain
LANG_DOMAIN = "kicad_amf_plugin"

TRANSLATION = [
    _('English'),
    _('Japanese'),
     _('Chinese')
]

from collections import  namedtuple

LanguageCodeName = namedtuple('LanguageCodeName',['Code','Name'])


# languages you want to support
SUPPORTED_LANG = { 
    wx.LANGUAGE_ENGLISH :  LanguageCodeName('en','English'),
    wx.LANGUAGE_JAPANESE_JAPAN :  LanguageCodeName('ja','Japanese'),
    wx.LANGUAGE_CHINESE_SIMPLIFIED :  LanguageCodeName('zh_CN','Chinese')
}
