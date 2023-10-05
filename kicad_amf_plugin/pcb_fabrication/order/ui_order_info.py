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

		m_radioBox3Choices = [ _(u"CN"), _(u"JP"), _(u"EU/USA") ]
		self.m_radioBox3 = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Order Region"), wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox3.SetSelection( 2 )
		sbSizer4.Add( self.m_radioBox3, 1, 0, 5 )

		self.m_bpButton1 = wx.BitmapButton( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BU_LEFT )

		self.m_bpButton1.SetBitmap( wx.Bitmap( self.GetImagePath( u"language.png" ), wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		sbSizer4.Add( self.m_bpButton1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer4, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Price detail") ), wx.VERTICAL )

		self.list_price_detail = wx.dataview.DataViewListCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_NO_HEADER|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		sbSizer1.Add( self.list_price_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Order Summary") ), wx.VERTICAL )

		self.list_order_summary = wx.dataview.DataViewListCtrl( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_NO_HEADER|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		sbSizer41.Add( self.list_order_summary, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )


		bSizer1.Add( sbSizer41, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )

		self.btn_update_price = wx.Button( self, wx.ID_ANY, _(u"Update Price"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_update_price, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_place_order = wx.Button( self, wx.ID_ANY, _(u"Place Order"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_place_order, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_menu3 = wx.Menu()
		self.Bind( wx.EVT_RIGHT_DOWN, self.UiOrderInfoOnContextMenu )


	def __del__( self ):
		pass

	def UiOrderInfoOnContextMenu( self, event ):
		self.PopupMenu( self.m_menu3, event.GetPosition() )

	# Virtual image path resolution method. Override this in your derived class.
	def GetImagePath( self, bitmap_path ):
		return bitmap_path


