# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from kicad_amf_plugin.icon import GetImagePath

import gettext
_ = gettext.gettext

###########################################################################
## Class UiOrderInfo
###########################################################################

class UiOrderInfo ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Preference") ), wx.HORIZONTAL )

		m_radioBox3Choices = [ _(u"简体中文"), _(u"日本语"), _(u"English") ]
		self.m_radioBox3 = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Language"), wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox3.SetSelection( 2 )
		sbSizer4.Add( self.m_radioBox3, 1, wx.ALL, 5 )

		self.m_button12 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Set Language"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )

		self.m_bitmap1 =wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(GetImagePath(
             "Huaqiu.png"), wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Price detail") ), wx.VERTICAL )

		self.list_price_detail = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.list_price_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"PCB Quantity"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"pcs"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )


		fgSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )


		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )


		sbSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.AddGrowableCol( 1 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Time"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer11.Add( self.m_staticText11, 0, wx.ALL, 5 )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.AddGrowableCol( 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText41 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer31.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Days"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer31.Add( self.m_staticText51, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer31, 1, wx.EXPAND, 5 )


		fgSizer11.Add( fgSizer21, 1, wx.EXPAND, 5 )


		sbSizer2.Add( fgSizer11, 1, wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.AddGrowableCol( 1 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Cost"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer12.Add( self.m_staticText12, 0, wx.ALL, 5 )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.AddGrowableCol( 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer32 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer32.AddGrowableCol( 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText42 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer32.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"$"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer32.Add( self.m_staticText52, 0, wx.ALL, 5 )


		fgSizer22.Add( fgSizer32, 1, wx.EXPAND, 5 )


		fgSizer12.Add( fgSizer22, 1, wx.EXPAND, 5 )


		sbSizer2.Add( fgSizer12, 1, wx.EXPAND, 5 )

		self.btn_update_price = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Update Price"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.btn_update_price, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_place_order = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Place Order"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.btn_place_order, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


