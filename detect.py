#!/usr/bin/python3

from datetime import *
import sys
from pprint import *

out_of_project_files = "/home/akbkuku/.youtube/"

sys.path.append("/home/akbkuku/.youtube")
from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey


api = GoogleAPIKey()
"""
ytd = YTData()
ytd.set_client(api.get_client_id(),api.get_client_secret())
ytd.connect()

pprint(ytd.get_video_list())
"""

# Connect to youtube api
yta = YTAnalytics()
yta.set_channel_id(api.channel_id)
yta.set_client(api.get_client_id(),api.get_client_secret())
yta.connect()
video_ids = [ 
    "p5o6NQmEA-8", # floppy
    "W3RhGGFiDt8", # mic
    "C_XdrXjYqGE" # tek
]

for video in video_ids:
    for day in [2,3,4]:
        pprint(yta.get_revenue(date.today()-timedelta(day),video_id=video))




