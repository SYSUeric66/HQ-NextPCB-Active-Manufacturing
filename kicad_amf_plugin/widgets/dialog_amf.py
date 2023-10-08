from . import validators
import os
import wx
import wx.lib.masked as masked
import urllib.request
import urllib.parse
import json
import re
from kicad_amf_plugin.utils.urlencodeform  import UrlEncodeForm
from collections import defaultdict
import locale
from datetime import datetime
import requests
import webbrowser

import pcbnew
from . import dialog_amf_base
from kicad_amf_plugin.kicad.fabrication_data_generator import FabricationDataGenerator
import gettext
_ = gettext.gettext


# Implementing AmfDialogBase

class AmfDialog(dialog_amf_base.AmfDialogBase):
    def __init__(self, parent):
        dialog_amf_base.AmfDialogBase.__init__(self, parent)

        self.board = pcbnew.GetBoard()

        boardWidth = pcbnew.ToMM(
            self.board.GetBoardEdgesBoundingBox().GetWidth())
        boardHeight = pcbnew.ToMM(
            self.board.GetBoardEdgesBoundingBox().GetHeight())
        designSettings = self.board.GetDesignSettings()
        boardThickness = designSettings.GetBoardThickness()
        minTraceWidth = designSettings.m_TrackMinWidth
        minTraceClearance = designSettings.m_MinClearance
        minHoleSize = designSettings.m_MinThroughDrill
        layerCount = self.board.GetCopperLayerCount()
        self.load_config_file()
        self.combo_layer_count.SetSelection(
            self.combo_layer_count.FindString(str(layerCount)))
        self.OnThicknessChangebyLayer(None)
        self.combo_layer_count.Enabled = False
        # self.m_placeOrderButton.Enabled = False
        self.edit_size_x.SetValue(str(boardWidth))
        self.edit_size_x.SetEditable(False)
        self.edit_size_y.SetValue(str(boardHeight))
        self.edit_size_y.SetEditable(False)
        # self.m_asmSizeXCtrl.SetValue(str(boardWidth))
        # self.m_asmSizeXCtrl.SetEditable(False)
        # self.m_asmSizeYCtrl.SetValue(str(boardHeight))
        # self.m_asmSizeYCtrl.SetEditable(False)
        self.SetBoardThickness(pcbnew.ToMM(boardThickness))
        self.SetMinTrace(pcbnew.ToMils(minTraceWidth),
                         pcbnew.ToMils(minTraceClearance))
        self.SetMinHole(pcbnew.ToMM(minHoleSize))
        self.combo_pcb_package_kind.SetSelection(0)
        self.OnPcbPackagingChanged(None)
        self.comb_margin_mode.SetSelection(0)
        self.OnMarginModeChanged(None)
        self.combo_surface_process.SetSelection(0)
        self.OnSurfaceProcessChanged(None)
        self.numericValidator = validators.NumericTextCtrlValidator()
        self.edit_panel_x.SetValidator(self.numericValidator)
        self.edit_panel_y.SetValidator(self.numericValidator)
        self.floatValidator = validators.FloatTextCtrlValidator()
        self.edit_margin_size.SetValidator(self.floatValidator)
        if layerCount == 2:
            self.m_innerCopperThicknessLabel.Enabled = False
            self.combo_inner_copper_thickness.Enabled = False
            self.m_blindViaLabel.Enabled = False
            self.combo_blind_via.Enabled = False
        else:
            self.m_innerCopperThicknessLabel.Enabled = True
            self.combo_inner_copper_thickness.Enabled = True
            self.m_blindViaLabel.Enabled = True
            self.combo_blind_via.Enabled = True
        self.m_template.SetSelection(0)
        self.OnTemplateChanged(None)
        self.OnPcbQuantityChanged(None)
        self.OnHDIChanged(None)
        # self.OnMaskColorChange(None)
        self.fabrication = None
        # self.SetSMTInfo()
        # self.SetDIPInfo()

    # Handlers for AmfDialogBase events.
    def OnTemplateChanged(self, event):
        if self.m_template.GetSelection() == 0 and self.m_notebook.PageCount > 1:
            self.m_notebook.RemovePage(1)
        elif self.m_template.GetSelection() == 1 and self.m_notebook.PageCount == 1:
            self.m_notebook.AddPage(self.m_panelAsm, _(u"PCB Assembly"), True)

    def OnPcbPackagingChanged(self, event):
        if self.combo_pcb_package_kind.GetSelection() == 0:
            self.m_sizeLabel.SetLabel('Size (single)')
            self.m_quantityLbel.SetLabel('Qty(single)')
            self.m_quantityUnit.SetLabel('Pcs')
            self.m_panelizeRuleLbel.Enabled = False
            self.m_panelizeXLabel.Enabled = False
            self.edit_panel_x.Enabled = False
            self.m_panelizeXUnit.Enabled = False
            self.m_panelizeYLabel.Enabled = False
            self.edit_panel_y.Enabled = False
            self.m_panelizeYUnit.Enabled = False
            self.m_marginLabel.Enabled = True
            self.comb_margin_mode.Enabled = True
            self.OnMarginModeChanged(None)
        else:
            self.m_sizeLabel.SetLabel('Size (set)')
            self.m_quantityLbel.SetLabel('Qty(Set)')
            self.m_quantityUnit.SetLabel('Set')
            self.m_panelizeRuleLbel.Enabled = True
            self.m_panelizeXLabel.Enabled = True
            self.edit_panel_x.Enabled = True
            self.edit_panel_x.SetEditable(True)
            self.m_panelizeXUnit.Enabled = True
            self.m_panelizeYLabel.Enabled = True
            self.edit_panel_y.Enabled = True
            self.edit_panel_y.SetEditable(True)
            self.m_panelizeYUnit.Enabled = True
            self.m_marginLabel.Enabled = True
            self.comb_margin_mode.Enabled = True
            self.OnMarginModeChanged(None)

    def OnMarginModeChanged(self, event):
        if self.comb_margin_mode.GetSelection() == 0:
            self.edit_margin_size.Enabled = False
            self.m_marginValueUnit.Enabled = False
        else:
            self.edit_margin_size.Enabled = True
            self.edit_margin_size.SetEditable(True)
            self.m_marginValueUnit.Enabled = True

    def OnSurfaceProcessChanged(self, event):
        if self.combo_surface_process.GetSelection() == 2:
            self.m_goldThicknessLabel.Enabled = True
            self.combo_gold_thickness.Enabled = True
        else:
            self.m_goldThicknessLabel.Enabled = False
            self.combo_gold_thickness.Enabled = False

    def OnPanelizeXChanged(self, event):
        if not self.edit_panel_x.Validate():
            wx.MessageBox("Panel Type X value isn't valid. Please input valid value.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return
        # self.m_asmQuantityCtrl.SetValue(str(self.GetPcbQuantity()))

    def OnPanelizeYChanged(self, event):
        if not self.edit_panel_y.Validate():
            wx.MessageBox("Panel Type Y value isn't valid. Please input valid value.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return
        # self.m_asmQuantityCtrl.SetValue(str(self.GetPcbQuantity()))

    def OnPcbQuantityChanged(self, event):
        # self.m_asmQuantityCtrl.SetValue(str(self.GetPcbQuantity()))
        return

    def OnHDIChanged(self, event):
        if self.combo_blind_via.GetSelection() == 1:
            self.m_hdiStructureLabel.Enabled = True
            self.combo_hdi_structure.Enabled = True
        else:
            self.m_hdiStructureLabel.Enabled = False
            self.combo_hdi_structure.Enabled = False

    def OnReportChanged(self, event):
        if self.comb_delivery_report.GetSelection() == 0 and self.combo_microsection_report.GetSelection() == 0:
            self.m_reportFormatLabel.Enabled = False
            self.comb_report_format.Enabled = False
        else:
            self.m_reportFormatLabel.Enabled = True
            self.comb_report_format.Enabled = True

    def OnMaskColorChange(self, event):
        self.combo_silk_screen_color.Clear()
        mask_color = self.combo_solder_color.GetString(
            self.combo_solder_color.GetSelection())
        val_list = self.config_json["rule"]["silkscreen"][mask_color]
        self.combo_silk_screen_color.Append(val_list)
        self.combo_silk_screen_color.SetSelection(0)

    def OnThicknessChangebyLayer(self, event):
        layer = self.combo_layer_count.GetString(
            self.combo_layer_count.GetSelection())
        self.combo_board_thickness.Clear()
        val_list = self.config_json["rule"]["thickness"][layer]
        self.combo_board_thickness.Append(val_list)

    def load_config_file(self):
        """Load config from config.json"""
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), "config.json")):
            wx.MessageBox("Load config json file failed.Please reinstall plugin.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return
        with open(os.path.join(os.path.dirname(__file__), "config.json")) as j:
            self.config_json = json.load(j)

    def init_fabrication(self):
        """Initialize the fabrication"""
        if not self.fabrication:
            self.fabrication = FabricationDataGenerator(self)

    # def OnDoDIPChanged( self, event ):
    #     if self.m_doDIPCtrl.GetSelection() == 0:
    #         self.m_dipComponentKindsCtrl.SetEditable(False)
    #         self.m_dipPadCountCtrl.SetEditable(False)
    #     else:
    #         self.m_dipComponentKindsCtrl.SetEditable(True)
    #         self.m_dipPadCountCtrl.SetEditable(True)

    def GetInfoFromSetting(self):
        if self.combo_pcb_package_kind.GetSelection() == 1 or self.combo_pcb_package_kind.GetSelection() == 2:
            if not self.edit_panel_x.Validate():
                wx.MessageBox(
                    "Panel Type X value isn't valid. Please input valid value.", "Error", wx.OK | wx.ICON_ERROR)
                return
            if not self.edit_panel_y.Validate():
                wx.MessageBox(
                    "Panel Type Y value isn't valid. Please input valid value.", "Error", wx.OK | wx.ICON_ERROR)
                return
        if self.edit_margin_size.Enabled:
            if not self.edit_margin_size.Validate():
                wx.MessageBox(
                    "Break-away Rail value isn't valid. Please input valid value.", "Error", wx.OK | wx.ICON_ERROR)
                return

        form = UrlEncodeForm()
        form.add_field('service', 'pcb')
        # self.combo_material_type.GetString(self.combo_material_type.GetSelection()))
        form.add_field('plate_type', 'Fr-4')
        layercount = int(self.combo_layer_count.GetString(
            self.combo_layer_count.GetSelection()))
        form.add_field('blayer', str(layercount))
        form.add_field('board_tg', 'TG130')  # TODO
        if self.combo_pcb_package_kind.GetSelection() == 0:
            form.add_field('units', '1')
        elif self.combo_pcb_package_kind.GetSelection() == 1:
            form.add_field('units', '3')
        else:
            form.add_field('units', '2')
        form.add_field('blength', str(round(self.GetPcbLength() / 10, 2)))
        form.add_field('bwidth', str(round(self.GetPcbWidth() / 10, 2)))
        if self.combo_pcb_package_kind.GetSelection() == 1 or self.combo_pcb_package_kind.GetSelection() == 2:
            form.add_field('layoutx', self.edit_panel_x.GetValue())
            form.add_field('layouty', self.edit_panel_y.GetValue())
        form.add_field('bcount', self.m_quantityCtrl.GetString(
            self.m_quantityCtrl.GetSelection()))
        form.add_field('sidedirection', self.GetMarginMode())
        if self.comb_margin_mode.GetSelection() != 0:
            form.add_field('sidewidth', self.edit_margin_size.GetValue())
        form.add_field('bheight', self.combo_board_thickness.GetString(
            self.combo_board_thickness.GetSelection()))
        form.add_field('copper', str(self.GetOuterCopperThickness()))
        if layercount > 2:
            form.add_field('insidecopper', str(self.GetInnerCopperThickness()))
            if self.combo_stackup.GetSelection() == 0:
                form.add_field('pressing', '')
            else:
                form.add_field('pressing', 'Customer Specified Stack up')
        else:
            form.add_field('insidecopper', '0')
            form.add_field('pressing', '')
        form.add_field('lineweight', str(self.GetMinTraceWidthAndClearance()))
        form.add_field('vias', str(self.GetMinHoleSize()))
        form.add_field('color', self.combo_solder_color.GetString(
            self.combo_solder_color.GetSelection()))
        form.add_field('charcolor', self.combo_silk_screen_color.GetString(
            self.combo_silk_screen_color.GetSelection()))
        form.add_field('cover', self.combo_solder_cover.GetString(
            self.combo_solder_cover.GetSelection()))
        form.add_field('spray', self.combo_surface_process.GetString(
            self.combo_surface_process.GetSelection()))
        if self.combo_surface_process.GetSelection() == 2:
            form.add_field('cjh', str(self.GetCJH()))

        form.add_field('impendance', str(self.combo_impedance.GetSelection()))
        form.add_field('bankong', str(self.combo_halfHole.GetSelection()))
        form.add_field('blind', self.GetBlindValue())
        form.add_field('via_in_pad', self.GetViaInPad())

        form.add_field('test', self.GetTestMethod())
        form.add_field('shipment_report', str(
            self.comb_delivery_report.GetSelection()))
        form.add_field('slice_report', str(
            self.combo_microsection_report.GetSelection()))
        form.add_field('report_type', str(self.GetReportType()))
        form.add_field('beveledge', str(self.combo_goldFinger.GetSelection()))
        form.add_field('review_file', self.GetReviewFile())
        form.add_field('has_period', self.GetHasPeriod())
        if self.comb_ul_mark.GetSelection() != 0:
            form.add_field('period_format', self.GetPeriodFormat())
        form.add_field('film_report', str(self.comb_film.GetSelection()))
        form.add_field('pcb_note', self.edit_special_request.GetValue())

        form.add_field('region_id', '211')  # TODO
        form.add_field('country', '211')  # TODO
        form.add_field('express', '31')  # TODO
        # form.add_field('express', '0')
        # form.add_field('expresstime', '3-5%20days')
        # form.add_field('calc_type', '0')
        # form.add_field('deltime', '72%20hours')
        # form.add_field('activity_code', '')
        # form.add_field('active', '')
        # form.add_field('history_pcb_order_sn', '0')
        # form.add_field('pbnum', '1')
        # form.add_field('isgerber', '1')
        # form.add_field('thermalc', '')
        # form.add_field('rogers', '')
        # form.add_field('holedensity', '0')
        # form.add_field('cjarea', '0')
        # form.add_field('testpoint', '0')
        # form.add_field('zknum', '0')
        # form.add_field('baobian', '')
        # form.add_field('pcscount', '20')
        # form.add_field('pcb_po_number', '')
        # form.add_field('pcb_note', '')
        # form.add_field('review_file', '0')
        # form.add_field('cross_board', '1')
        # form.add_field('user_stamp', '3')
        # form.add_field('paper', '1')
        # form.add_field('file_standard', '2')
        # form.add_field('acceptance', '1')

        self.form = form

    def OnUpdatePrice(self, event):
        self.GetInfoFromSetting()
        self.form.convert_to_dict()

        self.form.make_result()
        url = 'https://www.nextpcb.com/ajax/valuation'
        req1 = urllib.request.Request(url, data=self.form.form_data)
        fp = urllib.request.urlopen(req1)
        data = fp.read()
        self.m_priceDetailsViewListCtrl.DeleteAllItems()
        encoding = fp.info().get_content_charset('utf-8')
        quote = json.loads(data.decode(encoding))
        # text_file = open("d:\QuotePCB.txt", "w")
        # n = text_file.write(data.decode(encoding))
        # text_file.close()

        if quote['code'] != 200:
            wx.MessageBox(quote['msg'], "Error", wx.OK | wx.ICON_ERROR)
            return

        data = ['Fabrication:', '']
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        if 'discount' in quote['data']:
            value = '$' + str(quote['data']['pcb_total_original'])
            data = ['PCB Price', value]
            self.m_priceDetailsViewListCtrl.AppendItem(data)

            value = '$' + str(quote['data']['discount']
                              ['pcb']['discount_amount'])
            data = [quote['data']['discount']['pcb']['title'], value]
            self.m_priceDetailsViewListCtrl.AppendItem(data)
        else:
            value = '$' + str(quote['data']['pcb_total'])
            data = ['PCB Price', value]
            self.m_priceDetailsViewListCtrl.AppendItem(data)

        # freight_value = quote['data']['freight']
        # data = ['Shipping Cost', value]
        # self.m_priceDetailsViewListCtrl.AppendItem(data)
        # wx.MessageBox(f"freight_value:{freight_value}.total{quote['data']['total']}", "Help", style=wx.ICON_INFORMATION)

        value = '$' + \
            str(round(float(quote['data']['total']) -
                float(quote['data']['freight']), 2))
        data = ['Total', value]
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        value = quote['data']['delivery_date']
        data = ['Delivery Date', value]
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        locale.setlocale(locale.LC_ALL, '')
        deldate = str(quote['data']['delivery_date'][0:10])
        fabDueDate = str(
            (datetime.strptime(deldate, '%Y/%m/%d') - datetime.now()).days)

        value = str(round(quote['data']['weight'], 4)) + 'kg'
        data = ['Weight', value]
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        value = str(round(quote['data']['list']
                    ['pcb']['area'] / 10000, 4)) + '㎡'
        data = ['Area', value]
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        data = ['', '']
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        totalPrice = round(
            float(quote['data']['total']) - float(quote['data']['freight']), 2)

        value = '$' + str(totalPrice)
        data = ['Total Price', value]
        self.m_priceDetailsViewListCtrl.AppendItem(data)

        self.m_amountCtrl.SetLabel(str(self.GetPcbQuantity()))
        self.m_priceCtrl.SetLabel(str(totalPrice))
        if self.m_template.GetSelection() == 0:
            self.m_dueDateCtrl.SetLabel(
                str(self.GetDaysFromString(fabDueDate)))
        else:
            self.m_dueDateCtrl.SetLabel('-')

    def GetImagePath(self, bitmap_path):
        return os.path.join(os.path.dirname(__file__), bitmap_path)

    def GetPcbQuantity(self):
        n = int(self.m_quantityCtrl.GetString(
            self.m_quantityCtrl.GetSelection()))
        if self.combo_pcb_package_kind.GetSelection() == 1 or self.combo_pcb_package_kind.GetSelection() == 2:
            return n * int(self.edit_panel_x.GetValue()) * int(self.edit_panel_y.GetValue())
        else:
            return n

    def GetPcbLength(self):
        if self.combo_pcb_package_kind.GetSelection() == 0:
            if self.comb_margin_mode.GetSelection() == 1 or self.comb_margin_mode.GetSelection() == 3:
                return float(self.edit_size_x.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_x.GetValue())
        else:
            if self.comb_margin_mode.GetSelection() == 1 or self.comb_margin_mode.GetSelection() == 3:
                return float(self.edit_size_x.GetValue()) * int(self.edit_panel_x.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_x.GetValue()) * int(self.edit_panel_x.GetValue())

    def GetPcbWidth(self):
        if self.combo_pcb_package_kind.GetSelection() == 0:
            if self.comb_margin_mode.GetSelection() == 1 or self.comb_margin_mode.GetSelection() == 3:
                return float(self.edit_size_y.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_y.GetValue())
        else:
            if self.comb_margin_mode.GetSelection() == 1 or self.comb_margin_mode.GetSelection() == 3:
                return float(self.edit_size_y.GetValue()) * int(self.edit_panel_y.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_y.GetValue()) * int(self.edit_panel_y.GetValue())

    def GetMarginMode(self):
        if self.comb_margin_mode.GetSelection() == 0:
            return "N/A"
        elif self.comb_margin_mode.GetSelection() == 1:
            return "X"
        elif self.comb_margin_mode.GetSelection() == 2:
            return "Y"
        elif self.comb_margin_mode.GetSelection() == 3:
            return "XY"
        else:
            return "N/A"

    def GetOuterCopperThickness(self):
        if self.combo_outer_copper_thickness.GetSelection() == 0:
            return 1
        elif self.combo_outer_copper_thickness.GetSelection() == 1:
            return 2

    def GetInnerCopperThickness(self):
        if self.combo_inner_copper_thickness.GetSelection() == 0:
            return 0.5
        if self.combo_inner_copper_thickness.GetSelection() == 1:
            return 1
        elif self.combo_inner_copper_thickness.GetSelection() == 2:
            return 2

    def GetMinTraceWidthAndClearance(self):
        if self.combo_min_trace_width_clearance.GetSelection() == 0:
            return 10
        elif self.combo_min_trace_width_clearance.GetSelection() == 1:
            return 8
        elif self.combo_min_trace_width_clearance.GetSelection() == 2:
            return 6
        elif self.combo_min_trace_width_clearance.GetSelection() == 3:
            return 5
        elif self.combo_min_trace_width_clearance.GetSelection() == 4:
            return 4
        elif self.combo_min_trace_width_clearance.GetSelection() == 5:
            return 3.5
        else:
            return 10

    def GetMinHoleSize(self):
        if self.combo_min_hole_size.GetSelection() == 0:
            return 0.3
        elif self.combo_min_hole_size.GetSelection() == 1:
            return 0.25
        elif self.combo_min_hole_size.GetSelection() == 2:
            return 0.2
        elif self.combo_min_hole_size.GetSelection() == 3:
            return 0.15
        else:
            return 0.3

    def GetCJH(self):
        if self.combo_gold_thickness.GetSelection() == 0:
            return 1
        elif self.combo_gold_thickness.GetSelection() == 1:
            return 2
        elif self.combo_gold_thickness.GetSelection() == 2:
            return 3
        else:
            return 1

    def GetBlindValue(self):
        if self.combo_blind_via.GetSelection() == 0:
            return "0"
        elif self.combo_hdi_structure.GetSelection() == 0:
            return "1"
        elif self.combo_hdi_structure.GetSelection() == 1:
            return "2"
        elif self.combo_hdi_structure.GetSelection() == 2:
            return "3"

    def GetTestMethod(self):
        if self.comb_test_method.GetSelection() == 0:
            return 'Sample Test Free'
        elif self.comb_test_method.GetSelection() == 1:
            return 'Batch Flying Probe Test'
        elif self.comb_test_method.GetSelection() == 2:
            return 'Batch Fixture Test'

    def GetReviewFile(self):
        if self.comb_approve_gerber.GetSelection() == 0:
            return '0'
        else:
            return '2'

    def GetHasPeriod(self):
        if self.comb_ul_mark.GetSelection() == 0:
            return '2'
        else:
            return '6'

    def GetPeriodFormat(self):
        if self.comb_ul_mark.GetSelection() == 1:
            return '2'
        elif self.comb_ul_mark.GetSelection() == 2:
            return '1'

    def GetViaInPad(self):
        if self.combo_pad_hole.GetSelection() == 0:
            return 'N/A'
        else:
            return 'Have'

    def GetReportType(self):
        if self.comb_delivery_report.GetSelection() == 0 and self.combo_microsection_report.GetSelection() == 0:
            return 0
        elif self.comb_report_format.GetSelection() == 0:
            return 2
        elif self.comb_report_format.GetSelection() == 1:
            return 1

    def GetDaysFromString(self, str):
        numbers = re.findall('\d+', str)
        if '小时' in str:
            return int(int(numbers[0]) / 24)
        else:
            return int(numbers[0])

    def SetBoardThickness(self, thickness):
        for i in range(self.combo_board_thickness.GetCount()):
            if thickness <= float(self.combo_board_thickness.GetString(i)):
                self.combo_board_thickness.SetSelection(i)
                break

    def SetMinTrace(self, minTraceWidth, minTraceClearance):
        if minTraceWidth == 0 and minTraceClearance == 0:
            minTrace = 6
        elif minTraceWidth == 0:
            minTrace = minTraceClearance
        elif minTraceClearance == 0:
            minTrace = minTraceWidth
        else:
            minTrace = min(minTraceWidth, minTraceClearance)

        if minTrace == 0:
            minTrace = 6
            self.combo_min_trace_width_clearance.SetSelection(2)
        elif minTrace >= 10:
            minTrace = 10
            self.combo_min_trace_width_clearance.SetSelection(0)
        elif minTrace >= 8:
            minTrace = 8
            self.combo_min_trace_width_clearance.SetSelection(1)
        elif minTrace >= 6:
            minTrace = 6
            self.combo_min_trace_width_clearance.SetSelection(2)
        elif minTrace >= 5:
            minTrace = 5
            self.combo_min_trace_width_clearance.SetSelection(3)
        elif minTrace >= 4:
            minTrace = 4
            self.combo_min_trace_width_clearance.SetSelection(4)
        else:
            minTrace = 3.5
            self.combo_min_trace_width_clearance.SetSelection(5)

    def SetMinHole(self, minHoleSize):
        if minHoleSize == 0:
            minHoleSize = 0.3
            self.combo_min_hole_size.SetSelection(0)
        elif minHoleSize >= 0.3:
            minHoleSize = 0.3
            self.combo_min_hole_size.SetSelection(0)
        elif minHoleSize >= 0.25:
            minHoleSize = 0.25
            self.combo_min_hole_size.SetSelection(1)
        elif minHoleSize >= 0.2:
            minHoleSize = 0.2
            self.combo_min_hole_size.SetSelection(2)
        else:
            minHoleSize = 0.15
            self.combo_min_hole_size.SetSelection(3)

    def SetSMTInfo(self):
        smtPadCount = 0
        topSMT = False
        bottomSMT = False
        footprints = list(self.board.GetFootprints())
        footprints.sort(key=lambda x: x.GetReference())
        footprintReferecens = defaultdict(int)
        for i, footprint in enumerate(footprints):
            if footprint.GetAttributes() & pcbnew.FP_SMD == pcbnew.FP_SMD:
                # if not footprint.HasThroughHolePads():
                if footprint.GetLayer() == pcbnew.F_Cu:
                    topSMT = True
                elif footprint.GetLayer() == pcbnew.B_Cu:
                    bottomSMT = True
                footprintReferecens[str(footprint.GetFPID().GetLibItemName(
                )) + '&&&&' + footprint.GetValue().upper()] += 1
                smtPadCount += len(footprint.Pads())
                # pads = list(footprint.Pads())
                # for pad in pads:
                #     if pad.ShowPadAttr() == 'SMD':
                #         if pad.IsOnLayer(pcbnew.F_Cu) or pad.IsOnLayer(pcbnew.B_Cu):
                #             smtPadCount = smtPadCount + 1

        # self.m_smtSingleDouleSideCtrl.SetSelection(1 if topSMT and bottomSMT else 0)
        # self.m_smtComponentKindsCtrl.SetValue(str(len(footprintReferecens.items())))
        # self.m_smtPadCountCtrl.SetValue(str(smtPadCount))

    def generate_fabrication_data(self, e):
        """Generate fabrication data."""
        self.fabrication.fill_zones()
        self.fabrication.generate_geber(None)
        self.fabrication.generate_excellon()
        self.fabrication.zip_gerber_excellon()

    def OnPlaceOrder(self, e):
        self.m_placeOrderButton.Enabled = False
        try:
            wx.BeginBusyCursor()
            self.init_fabrication()
            self.generate_fabrication_data(e)
            self.place_order_request()
        finally:
            wx.EndBusyCursor()
            self.m_placeOrderButton.Enabled = True

    def place_order_request(self):
        zipname = f"GERBER-{self.fabrication.filename.split('.')[0]}.zip"
        zipfile = os.path.join(self.fabrication.outputdir, zipname)
        files = {'file': open(zipfile, 'rb')}
        upload_url = "https://www.nextpcb.com/Upfile/kiCadUpFile"
        self.GetInfoFromSetting()
        self.form.add_field('type', 'pcbfile')
        self.form.convert_to_dict()
        self.form.form_dict['blength'] = str(round(self.GetPcbLength(), 2))
        self.form.form_dict['bwidth'] = str(round(self.GetPcbWidth(), 2))
        rsp = requests.post(
            upload_url,
            files=files,
            data=self.form.form_dict
        )
        urls = json.loads(rsp.content)
        uat_url = str(urls['redirect'])
        webbrowser.open(uat_url)

    # def SetDIPInfo( self ):
    #     dipPadCount = 0
    #     footprints = list(self.board.GetFootprints())
    #     footprints.sort(key=lambda x: x.GetReference())
    #     footprintReferecens = defaultdict(int)
    #     for i, footprint in enumerate(footprints):
    #         if footprint.GetAttributes() & pcbnew.FP_THROUGH_HOLE == pcbnew.FP_THROUGH_HOLE:
    #         # if footprint.HasThroughHolePads():
    #             footprintReferecens[str(footprint.GetFPID().GetLibItemName()) + '&&&&' + footprint.GetValue().upper()] += 1
    #             dipPadCount += len(footprint.Pads())

    #     self.m_doDIPCtrl.SetSelection(1 if dipPadCount > 0 else 0)
    #     self.m_dipComponentKindsCtrl.SetValue(str(len(footprintReferecens.items())))
    #     self.m_dipPadCountCtrl.SetValue(str(dipPadCount))
    #     self.OnDoDIPChanged(None)
