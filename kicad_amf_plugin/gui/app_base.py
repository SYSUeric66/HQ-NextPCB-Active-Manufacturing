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
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
import builtins
import sys
import os
from kicad_amf_plugin import PLUGIN_ROOT
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
    def OnInit(self):
        self.Init()  # InspectionMixin
        # work around for Python stealing "_"
        sys.displayhook = _displayHook
        self.appName = "kicad-amf"
        self.setup_locale_config()
        self.locale = None
        wx.Locale.AddCatalogLookupPathPrefix(
            os.path.join(PLUGIN_ROOT, 'language','locale'))
        self.updateLanguage(int(self.appConfig.Read(u"Language")))
        return True

    def setup_locale_config(self):
        sp = wx.StandardPaths.Get()
        self.configLoc = sp.GetUserConfigDir()
        self.configLoc = os.path.join(self.configLoc, self.appName)

        if not os.path.exists(self.configLoc):
            os.mkdir(self.configLoc)

        self.appConfig = wx.FileConfig(appName=self.appName,
                                       vendorName=u'NextPCB',
                                       localFilename=os.path.join(
                                           self.configLoc, "AppConfig"))

        if not self.appConfig.HasEntry('Language'):
            # on first run we default to en
            #TODO - Read KiCad's config file
            self.appConfig.Write(key='Language', value=str(int(wx.LANGUAGE_ENGLISH)))
        self.appConfig.Write(key='Language', value=str(int(wx.LANGUAGE_ENGLISH)))
        self.appConfig.Flush()

    def updateLanguage(self, lang : int):
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
