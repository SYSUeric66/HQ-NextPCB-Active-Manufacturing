# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class UiBaseInfo
###########################################################################


class UiBaseInfo (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(421, 301), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos,
                          size=size, style=style, name=name)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Base Info"), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Material Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        fgSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        m_choice2Choices = []
        self.m_choice2 = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        fgSizer2.Add(self.m_choice2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Layer Count", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer2.Add(fgSizer2, 0, wx.EXPAND, 5)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.AddGrowableCol(1)
        fgSizer3.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Board Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        m_choice3Choices = []
        self.m_choice3 = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        fgSizer3.Add(self.m_choice3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText51 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Qty(single)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        fgSizer3.Add(self.m_staticText51, 0, wx.ALL, 5)

        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        m_choice4Choices = []
        self.m_choice4 = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0)
        self.m_choice4.SetSelection(0)
        fgSizer21.Add(self.m_choice4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText71 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)

        fgSizer21.Add(self.m_staticText71, 0, wx.ALL, 5)

        fgSizer3.Add(fgSizer21, 1, wx.EXPAND, 5)

        sbSizer2.Add(fgSizer3, 0, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Panel Type"), wx.VERTICAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText8 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        fgSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        fgSizer6 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer6.AddGrowableCol(0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl3 = wx.TextCtrl(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        fgSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer6, 1, wx.EXPAND, 5)

        self.m_staticText81 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)

        fgSizer4.Add(self.m_staticText81, 0, wx.ALL, 5)

        fgSizer61 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer61.AddGrowableCol(0)
        fgSizer61.SetFlexibleDirection(wx.BOTH)
        fgSizer61.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl31 = wx.TextCtrl(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer61.Add(self.m_textCtrl31, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText101 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)

        fgSizer61.Add(self.m_staticText101, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer61, 1, wx.EXPAND, 5)

        sbSizer21.Add(fgSizer4, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer21, 1, wx.EXPAND, 5)

        sbSizer211 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Size (single)"), wx.VERTICAL)

        fgSizer41 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer41.AddGrowableCol(1)
        fgSizer41.SetFlexibleDirection(wx.BOTH)
        fgSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText82 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText82.Wrap(-1)

        fgSizer41.Add(self.m_staticText82, 0, wx.ALL, 5)

        fgSizer62 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer62.AddGrowableCol(0)
        fgSizer62.SetFlexibleDirection(wx.BOTH)
        fgSizer62.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl32 = wx.TextCtrl(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer62.Add(self.m_textCtrl32, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText102 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText102.Wrap(-1)

        fgSizer62.Add(self.m_staticText102, 0, wx.ALL, 5)

        fgSizer41.Add(fgSizer62, 1, wx.EXPAND, 5)

        self.m_staticText811 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText811.Wrap(-1)

        fgSizer41.Add(self.m_staticText811, 0, wx.ALL, 5)

        fgSizer611 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer611.AddGrowableCol(0)
        fgSizer611.SetFlexibleDirection(wx.BOTH)
        fgSizer611.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl311 = wx.TextCtrl(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer611.Add(self.m_textCtrl311, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText1011 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1011.Wrap(-1)

        fgSizer611.Add(self.m_staticText1011, 0, wx.ALL, 5)

        fgSizer41.Add(fgSizer611, 1, wx.EXPAND, 5)

        sbSizer211.Add(fgSizer41, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer211, 1, wx.EXPAND, 5)

        sbSizer2.Add(bSizer2, 0, wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Break-away Rail"), wx.VERTICAL)

        fgSizer24 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer24.AddGrowableCol(1)
        fgSizer24.SetFlexibleDirection(wx.BOTH)
        fgSizer24.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        m_choice9Choices = []
        self.m_choice9 = wx.Choice(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0)
        self.m_choice9.SetSelection(0)
        fgSizer24.Add(self.m_choice9, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer24.Add(self.m_textCtrl16, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText39 = wx.StaticText(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)

        fgSizer24.Add(self.m_staticText39, 0, wx.ALL, 5)

        sbSizer12.Add(fgSizer24, 1, wx.EXPAND, 5)

        sbSizer2.Add(sbSizer12, 0, wx.EXPAND, 5)

        self.SetSizer(sbSizer2)
        self.Layout()

    def __del__(self):
        pass
