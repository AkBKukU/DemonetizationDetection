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
ytd = YTData()
ytd.set_channel_id(api.channel_id)
ytd.set_client(api.get_client_id(),api.get_client_secret())
ytd.connect()
#ytd.get_video_list()

#videos = ytd.get_video_list()


# Connect to youtube api
yta = YTAnalytics()
yta.set_channel_id(api.channel_id)
yta.set_client(api.get_client_id(),api.get_client_secret())
yta.connect()
videos = [ 
   [ "p5o6NQmEA-8","floppy","" ,[],[]],
   [ "GAk2YT8NwCc","changer","",[],[] ],
   [ "W3RhGGFiDt8","mic","" ,[],[]], 
   [ "C_XdrXjYqGE", "tek","",[],[] ]
]
days = [4,3,2]
for video in videos:
    for day in days:
        video[3].append(yta.get_views(date.today()-timedelta(day),video_id=video[0]))

for video in videos:
    for day in days:
        video[4].append(yta.get_monetizedPlaybacks(date.today()-timedelta(day),video_id=video[0]))

pprint(videos)

