
from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.pcb_fabrication.base.base_info_view import BaseInfoView
from kicad_amf_plugin.pcb_fabrication.process.process_info_view import ProcessInfoView
from kicad_amf_plugin.pcb_fabrication.special_process.special_process_view import SpecialProcessView
from kicad_amf_plugin.pcb_fabrication.personalized.personalized_info_view import PersonalizedInfoView
from kicad_amf_plugin.gui.summary.summary_panel import SummaryPanel
from kicad_amf_plugin.gui.event.pcb_fabrication_evt_list import EVT_LAYER_COUNT_CHANGE ,EVT_UPDATE_PRICE ,EVT_PLACE_ORDER
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from kicad_amf_plugin.kicad.fabrication_data_generator import FabricationDataGenerator
from kicad_amf_plugin.api.base_request import BaseRequest
from kicad_amf_plugin.utils.request_helper import RequestHelper
import wx
import wx.xrc
import wx.dataview
import urllib
import requests
import webbrowser
import json
from urllib import parse
from kicad_amf_plugin.order.order_region import  OrderRegion ,URL_KIND

class MainFrame (wx.Frame):

    def __init__(self, board_manager: BoardManager,  parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"HQ NextPCB Active Manufacturing"),
                          pos=wx.DefaultPosition, size=wx.Size(900, 600), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self._board_manager = board_manager
        self._fabrication_data_gen = None
        self.init_ui()

    def init_ui(self):
        wx.SizerFlags.DisableConsistencyChecks()
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        pcb_fab_panel = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
        pcb_fab_panel.SetScrollRate(10, 10)
        lay_pcb_fab_panel = wx.BoxSizer(wx.VERTICAL)

        self.base_info_panel = BaseInfoView(pcb_fab_panel, self._board_manager)
        lay_pcb_fab_panel.Add(self.base_info_panel, 0, wx.ALL | wx.EXPAND, 5)

        self.process_info_panel = ProcessInfoView(
            pcb_fab_panel, self._board_manager)
        lay_pcb_fab_panel.Add(self.process_info_panel,
                              0, wx.ALL | wx.EXPAND, 5)

        self.special_process_panel = SpecialProcessView(
            pcb_fab_panel, self._board_manager)
        lay_pcb_fab_panel.Add(self.special_process_panel,
                              0, wx.ALL | wx.EXPAND, 5)

        self.personalized_service = PersonalizedInfoView(
            pcb_fab_panel)
        lay_pcb_fab_panel.Add(self.personalized_service,
                              0, wx.ALL | wx.EXPAND, 5)

        pcb_fab_panel.SetSizer(lay_pcb_fab_panel)
        pcb_fab_panel.Layout()

        self.summary_view = SummaryPanel(self)

        main_sizer.Add(pcb_fab_panel, 1, wx.EXPAND, 8)
        main_sizer.Add(self.summary_view, 0, wx.EXPAND, 8)

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
    def fabrication_data_generator(self):
        if self._fabrication_data_gen is None:
            self._fabrication_data_gen = FabricationDataGenerator(self._board_manager.board)
        return self._fabrication_data_gen

    @property
    def query_price_form(self):
        return  dict(filter(lambda elem: elem[1] is not None, {
            **(BaseRequest().__dict__),
            **(self.base_info_panel.base_info.__dict__),
            **(self.process_info_panel.process_info.__dict__),
            **(self.special_process_panel.special_process_info.__dict__),
            **(self.personalized_service.personalized_info.__dict__),
        }.items()))
    

    @property
    def place_order_form(self):
        return  {
            **(BaseRequest().__dict__),
            **(self.base_info_panel.base_info.__dict__),
            **(self.process_info_panel.process_info.__dict__),
            **(self.special_process_panel.special_process_info.__dict__),
            **(self.personalized_service.personalized_info.__dict__),
            'type' : 'pcbfile'
        }

    def on_update_price(self, evt):
        url = OrderRegion.get_url(SETTING_MANAGER.order_region ,URL_KIND.QUERY_PRICE)
        if url is None:
            wx.MessageBox(_("No available url for querying price in current region"))
            return
        print(RequestHelper.convert_dict_to_request_data(self.query_price_form))
        rep = urllib.request.Request(url, data= RequestHelper.convert_dict_to_request_data(self.query_price_form))
        fp = urllib.request.urlopen(rep)
        data = fp.read()
        encoding = fp.info().get_content_charset('utf-8')
        quote = json.loads(data.decode(encoding))
        summary = quote['data']['list']
        summary['pcb_count'] = self.base_info_panel.get_pcb_count()
        summary['day'] = 0
        if 'pcb' in summary and 'deltime' in summary['pcb']:
            day = str(summary['pcb']['deltime']).split(' ')
            if len(day) == 2:
                if day[1] ==  'hours':
                     days = int(day[0])/24
                     summary['day'] =  int(days) if int(days) != 0 else  days
                else:
                    summary['day'] = int(day[0])
        self.summary_view.on_price_updated(summary)

    def on_place_order(self , evt):
        url = OrderRegion.get_url(SETTING_MANAGER.order_region ,URL_KIND.PLACE_ORDER)
        if url is None:
            wx.MessageBox(_("No available url for placing order in current region"))
            return
        with self.fabrication_data_generator.create_kicad_pcb_file() as zipfile :
            upload_url = "https://www.nextpcb.com/Upfile/kiCadUpFile"
            rsp = requests.post(
                upload_url,
                files = {
                    "file" :  open(zipfile, 'rb')
                },
                data = self.place_order_form
            )
            urls = json.loads(rsp.content)
            uat_url = str(urls['redirect'])
            webbrowser.open(uat_url)        



