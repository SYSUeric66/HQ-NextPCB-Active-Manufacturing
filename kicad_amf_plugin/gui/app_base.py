# -*- coding: utf-8 -*-
#
# Author:   Werner F. Bruhin
# Purpose:  how to I18N enable an application
#
# Inspired by the I18N wxPython demo and the Internationalization page on
# the wxPython wiki.
#

from wx.lib.mixins.inspection import InspectionMixin
from kicad_amf_plugin.language.lang_const import SUPPORTED_LANG, LANG_DOMAIN
import builtins
import sys
import os
from kicad_amf_plugin import PLUGIN_ROOT
from kicad_amf_plugin.gui.event.locale_change_evt import EVT_CHANGE_LOCALE
import wx
# add translation macro to builtin similar to what gettext does
builtins.__dict__['_'] = wx.GetTranslation


def _displayHook(obj):
    if obj is not None:
        print(repr(obj))


class BaseApp(wx.App, InspectionMixin):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect, filename, useBestVisual, clearSigInt)
        self.frame = None

    def OnInit(self):
        self.Init()  # InspectionMixin
        # work around for Python stealing "_"
        sys.displayhook = _displayHook
        self.locale = None
        wx.Locale.AddCatalogLookupPathPrefix(
            os.path.join(PLUGIN_ROOT, 'language', 'locale'))
        from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
        self.Bind(EVT_CHANGE_LOCALE, self.on_locale_changed)
        self.update_language(SETTING_MANAGER.language)
        SETTING_MANAGER.register_app(self)
        self.startup_dialog()
        return True

    def on_locale_changed(self, evt):
        self.update_language(evt.GetInt())
        info = wx.MessageDialog(self.frame, _('Restart the plugin to apply the new locale'),
                               _('Tip'),
                               wx.OK | wx.ICON_INFORMATION
                               )
        info.ShowModal()
        info.Destroy()


    def update_language(self, lang: int):
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

    def startup_dialog(self):
        from kicad_amf_plugin.gui.main_dialog import MainWindow
        self.frame = MainWindow(None)
        self.frame.ShowModal()
