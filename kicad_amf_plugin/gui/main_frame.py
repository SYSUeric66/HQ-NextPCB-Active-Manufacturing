
from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.pcb_fabrication.base.base_info_view import BaseInfoView
from kicad_amf_plugin.pcb_fabrication.process.process_info_view import ProcessInfoView
from kicad_amf_plugin.pcb_fabrication.special_process.special_process_view import SpecialProcessView
from kicad_amf_plugin.pcb_fabrication.personalized.personalized_info_view import PersonalizedInfoView
from kicad_amf_plugin.gui.summary.summary_panel import SummaryPanel
from kicad_amf_plugin.gui.event.pcb_fabrication_evt_list import EVT_LAYER_COUNT_CHANGE ,EVT_UPDATE_PRICE ,EVT_PLACE_ORDER
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from kicad_amf_plugin.utils.base_request import BaseRequest
import wx
import wx.xrc
import wx.dataview
import urllib
import requests
import webbrowser
import json
from urllib import parse
from kicad_amf_plugin.order.order_region import  OrderRegion

class MainFrame (wx.Frame):

    def __init__(self, board_manager: BoardManager,  parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"HQ NextPCB Active Manufacturing"),
                          pos=wx.DefaultPosition, size=wx.Size(900, 600), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        wx.SizerFlags.DisableConsistencyChecks()
        self.board_manager = board_manager
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        pcb_fab_panel = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
        pcb_fab_panel.SetScrollRate(10, 10)
        lay_pcb_fab_panel = wx.BoxSizer(wx.VERTICAL)

        self.base_info_panel = BaseInfoView(pcb_fab_panel, self.board_manager)
        lay_pcb_fab_panel.Add(self.base_info_panel, 0, wx.ALL | wx.EXPAND, 5)

        self.process_info_panel = ProcessInfoView(
            pcb_fab_panel, self.board_manager)
        lay_pcb_fab_panel.Add(self.process_info_panel,
                              0, wx.ALL | wx.EXPAND, 5)

        self.special_process_panel = SpecialProcessView(
            pcb_fab_panel, self.board_manager)
        lay_pcb_fab_panel.Add(self.special_process_panel,
                              0, wx.ALL | wx.EXPAND, 5)

        self.personalized_service = PersonalizedInfoView(
            pcb_fab_panel)
        lay_pcb_fab_panel.Add(self.personalized_service,
                              0, wx.ALL | wx.EXPAND, 5)

        pcb_fab_panel.SetSizer(lay_pcb_fab_panel)
        pcb_fab_panel.Layout()

        self.order_info_view = SummaryPanel(self)

        main_sizer.Add(pcb_fab_panel, 1, wx.EXPAND, 8)
        main_sizer.Add(self.order_info_view, 0, wx.EXPAND, 8)

        self.Bind(EVT_LAYER_COUNT_CHANGE,
                  self.process_info_panel.on_layer_count_changed)
        self.Bind(EVT_LAYER_COUNT_CHANGE,
                  self.special_process_panel.on_layer_count_changed)
        self.Bind(EVT_UPDATE_PRICE , self.on_update_price)
        self.Bind(EVT_PLACE_ORDER , self.on_place_order)

        for i in self.base_info_panel, self.process_info_panel:
            i.init()

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    @property
    def query_price_form(self):
        return  list(dict(filter(lambda elem: elem[1] is not None, {
            **(BaseRequest().__dict__),
            **(self.base_info_panel.base_info.__dict__),
            **(self.process_info_panel.process_info.__dict__),
            **(self.special_process_panel.special_process_info.__dict__),
            **(self.personalized_service.personalized_info.__dict__),
        }.items())).items())

    def on_update_price(self, event):
        url = OrderRegion.get_order_url(SETTING_MANAGER.order_region)
        if url is None:
            # NOTE shall not come here
            return
        form = self.query_price_form
        print(form)
        print( parse.urlencode(form).encode())
        req1 = urllib.request.Request(url, data= parse.urlencode(form).encode())
        fp = urllib.request.urlopen(req1)
        data = fp.read()
        encoding = fp.info().get_content_charset('utf-8')
        quote = json.loads(data.decode(encoding))
        print(quote)

    def on_place_order(self):
        pass