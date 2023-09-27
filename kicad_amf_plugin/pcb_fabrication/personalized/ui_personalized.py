# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class UiPersonalizedService
###########################################################################

class UiPersonalizedService ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 512,366 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		labelProcessInfo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Personalized Service") ), wx.VERTICAL )

		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText401 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Electrical Test"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401, 0, wx.ALL, 5 )

		m_choice111Choices = []
		self.m_choice111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice111Choices, 0 )
		self.m_choice111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4011 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Approve Working Gerber"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4011.Wrap( -1 )

		fgSizer25.Add( self.m_staticText4011, 0, wx.ALL, 5 )

		m_choice1111Choices = []
		self.m_choice1111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1111Choices, 0 )
		self.m_choice1111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice1111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Delivery Report"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText40111, 0, wx.ALL, 5 )

		m_choice11111Choices = []
		self.m_choice11111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11111Choices, 0 )
		self.m_choice11111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice11111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText401111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Microsection Analysis Report"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401111, 0, wx.ALL, 5 )

		m_choice111111Choices = []
		self.m_choice111111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice111111Choices, 0 )
		self.m_choice111111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice111111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4011111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Report Format"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4011111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText4011111, 0, wx.ALL, 5 )

		m_choice1111111Choices = []
		self.m_choice1111111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1111111Choices, 0 )
		self.m_choice1111111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice1111111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40111111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"UL Mark"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40111111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText40111111, 0, wx.ALL, 5 )

		m_choice11111111Choices = []
		self.m_choice11111111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11111111Choices, 0 )
		self.m_choice11111111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice11111111, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText401111111 = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Film"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401111111.Wrap( -1 )

		fgSizer25.Add( self.m_staticText401111111, 0, wx.ALL, 5 )

		m_choice111111111Choices = []
		self.m_choice111111111 = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice111111111Choices, 0 )
		self.m_choice111111111.SetSelection( 0 )
		fgSizer25.Add( self.m_choice111111111, 0, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( fgSizer25, 0, wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"Special Request") ), wx.VERTICAL )

		self.m_textCtrl17 = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_textCtrl17, 1, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( sbSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( labelProcessInfo )
		self.Layout()

	def __del__( self ):
		pass


