import json
import random
import time
import webbrowser
import requests
from six.moves import _thread
import wx

from kicad_amf_plugin.kicad.fabrication_data_generator import FabricationDataGenerator
from kicad_amf_plugin.order.order_region import URL_KIND, OrderRegion
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from .fabrication_data_generator_evt import (
    FabricationDataGenEvent,
    fabricationDataGenerateResult,
    GenerateStatus,
)


class CountingThread:
    def __init__(self, win) -> None:
        self.win = win
        self.count = 0
        self.should_stop = False
        _thread.start_new_thread(self.Run, ())

    def stop(self):
        self.should_stop = True

    def Run(self):
        while not self.should_stop:
            time.sleep(0.01)
            if self.count < GenerateStatus.MAX_PROGRESS - 10:
                self.count = self.count + 1
            evt = FabricationDataGenEvent(fabricationDataGenerateResult)
            evt.SetMyVal(GenerateStatus(GenerateStatus.RUNNING, "", self.count))
            wx.PostEvent(self.win, event=evt)


class DataGenThread:
    def __init__(self, win: wx.Window, gen: FabricationDataGenerator, form, url):
        self.win = win
        self.fabrication_data_generator = gen
        self.place_order_form = form
        self._url = url

    def Start(self):
        self.counting_thread = CountingThread(self.win)
        _thread.start_new_thread(self.Run, ())

    def Run(self):
        try:
            with self.fabrication_data_generator.create_kicad_pcb_file() as zipfile:
                rsp = requests.post(
                    self._url,
                    files={"file": open(zipfile, "rb")},
                    data=self.place_order_form,
                )
                urls = json.loads(rsp.content)
                for key in "url", "redirect":
                    if key in urls:
                        uat_url = str(urls[key])
                        webbrowser.open(uat_url)
                        evt = FabricationDataGenEvent(fabricationDataGenerateResult)
                        evt.SetMyVal(GenerateStatus(GenerateStatus.SUCCESS))
                        wx.PostEvent(self.win, event=evt)
                        return
                raise Exception("No available order url in the response")
        except Exception as e:
            evt = FabricationDataGenEvent(fabricationDataGenerateResult)
            evt.SetMyVal(GenerateStatus(GenerateStatus.FAILED, str(e)))
            wx.PostEvent(self.win, event=evt)
        finally:
            self.counting_thread.stop()
