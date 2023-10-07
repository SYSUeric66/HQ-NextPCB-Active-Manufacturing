# -*- coding: utf-8 -*-
#
# Author:   Werner F. Bruhin
# Purpose:  how to I18N enable an application
#
# Inspired by the I18N wxPython demo and the Internationalization page on
# the wxPython wiki.
#

from wx.lib.mixins.inspection import InspectionMixin
from  kicad_amf_plugin.language.lang_const  import SUPPORTED_LANG, LANG_DOMAIN
import builtins
import sys
import os
from kicad_amf_plugin import PLUGIN_ROOT
from kicad_amf_plugin.gui.event.locale_change_evt import  EVT_CHANGE_LOCALE
import wx


# Install a custom displayhook to keep Python from setting the global
# _ (underscore) to the value of the last evaluated expression.  If
# we don't do this, our mapping of _ to gettext can get overwritten.
# This is useful/needed in interactive debugging with PyShell.


def _displayHook(obj):
    if obj is not None:
        print(repr(obj))


# add translation macro to builtin similar to what gettext does
builtins.__dict__['_'] = wx.GetTranslation


class BaseApp(wx.App, InspectionMixin):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect, filename, useBestVisual, clearSigInt)


    def OnInit(self):
        self.Init()  # InspectionMixin
        # work around for Python stealing "_"
        sys.displayhook = _displayHook
        self.locale = None
        wx.Locale.AddCatalogLookupPathPrefix(
            os.path.join(PLUGIN_ROOT, 'language','locale'))
        from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER 
        SETTING_MANAGER.register_app(self)
        self.Bind(EVT_CHANGE_LOCALE, self.update_language)        
        self.update_language(SETTING_MANAGER.language)
        return True

    def update_language(self, evt ):
        lang = evt if isinstance(evt,int) else  evt.GetInt()
        if lang in SUPPORTED_LANG:
            selLang = lang
        else:
            selLang = wx.LANGUAGE_ENGLISH
        if self.locale:
            assert sys.getrefcount(self.locale) <= 2
            del self.locale

        self.locale = wx.Locale(selLang)
        if self.locale.IsOk():
            self.locale.AddCatalog(LANG_DOMAIN)
        else:
            self.locale = None
