# -*- coding: utf-8 -*-

from handlers.SimHistoryHandler import *
from handlers.SimFabrikHandler import *
from handlers.SimRealtimeHandler import *
from handlers.SimReportHandler import *

urls = [
    (r"/v1.0/stonefabs", listStoneFabs),
    (r"/v1.0/stonefab/([0-9]+)", listFabInfo),
    (r"/v1.0/stonefab/([0-9]+)/devices", listFabDevices),
    (r"/v1.0/stonefab/([0-9]+)/rtshort/device/([a-z]{2,3}[0-9]+[a-z]?)", devRTShortData),
    (r"/v1.0/stonefab/([0-9]+)/rtmore/device/([a-z]{2,3}[0-9]+[a-z]?)", devRTMoreData),
    (r"/v1.0/stonefab/([0-9]+)/hsweb/devices", hsDevices),
    (r"/v1.0/stonefab/([0-9]+)/hsweb/device/([a-z]{2,3}[0-9]+[a-z]?)", hsDevContent),
    (r"/v1.0/stonefab/([0-9]+)/hsdata/device/([a-z]{2,3}[0-9]+[a-z]?)/([a-z]+)", hsDevData),
    (r"/v1.0/stonefab/([0-9]+)/report/device/([a-z]{2,3}[0-9]+[a-z]?)/([a-z]+)", reportData),
]