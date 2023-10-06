# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc




###########################################################################
## Class UiPersonalizedService
###########################################################################

class UiPersonalizedService ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 459,389 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		labelProcessInfo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Personalized Service") ), wx.VERTICAL )

		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText401 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Electrical Test"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401, 0, wx.ALL, 5 )

		comb_test_methodChoices = []
		self.comb_test_method = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_test_methodChoices, 0 )
		self.comb_test_method.SetSelection( 0 )
		fgSizer25.Add( self.comb_test_method, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4011 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Approve Working Gerber"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4011.Wrap( -1 )

		fgSizer25.Add( self.m_staticText4011, 0, wx.ALL, 5 )

		comb_approve_gerberChoices = []
		self.comb_approve_gerber = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_approve_gerberChoices, 0 )
		self.comb_approve_gerber.SetSelection( 0 )
		fgSizer25.Add( self.comb_approve_gerber, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Delivery Report"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText40111, 0, wx.ALL, 5 )

		comb_delivery_reportChoices = []
		self.comb_delivery_report = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_delivery_reportChoices, 0 )
		self.comb_delivery_report.SetSelection( 0 )
		fgSizer25.Add( self.comb_delivery_report, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText401111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Microsection Analysis Report"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401111, 0, wx.ALL, 5 )

		comb_analysis_reportChoices = []
		self.comb_analysis_report = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_analysis_reportChoices, 0 )
		self.comb_analysis_report.SetSelection( 0 )
		fgSizer25.Add( self.comb_analysis_report, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4011111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Report Format"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4011111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText4011111, 0, wx.ALL, 5 )

		comb_report_formatChoices = []
		self.comb_report_format = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_report_formatChoices, 0 )
		self.comb_report_format.SetSelection( 0 )
		fgSizer25.Add( self.comb_report_format, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40111111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"UL Mark"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40111111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText40111111, 0, wx.ALL, 5 )

		comb_ul_markChoices = []
		self.comb_ul_mark = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_ul_markChoices, 0 )
		self.comb_ul_mark.SetSelection( 0 )
		fgSizer25.Add( self.comb_ul_mark, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText401111111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Film"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401111111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401111111, 0, wx.ALL, 5 )

		comb_filmChoices = []
		self.comb_film = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_filmChoices, 0 )
		self.comb_film.SetSelection( 0 )
		fgSizer25.Add( self.comb_film, 0, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( fgSizer25, 0, wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Special Request") ), wx.VERTICAL )

		self.edit_special_request = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.edit_special_request, 1, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( sbSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( labelProcessInfo )
		self.Layout()

	def __del__( self ):
		pass


