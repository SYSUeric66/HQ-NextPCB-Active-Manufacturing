from collections import namedtuple
import wx
_ = wx.GetTranslation

TRANSLATION = [
    _('English'),
    _('Japanese'),
    _('Chinese')
]

LanguageCodeName = namedtuple('LanguageCodeName', ['Code', 'Name'])

# languages you want to support
SUPPORTED_LANG = {
    wx.LANGUAGE_ENGLISH:  LanguageCodeName('en', 'English'),
    wx.LANGUAGE_JAPANESE_JAPAN:  LanguageCodeName('ja', 'Japanese'),
    wx.LANGUAGE_CHINESE_SIMPLIFIED:  LanguageCodeName('zh_CN', 'Chinese')
}
