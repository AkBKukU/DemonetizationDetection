#!/usr/bin/python3

import sys
from datetime import *
from pprint import *

out_of_project_files = "/home/akbkuku/.youtube/"

sys.path.append("/home/akbkuku/.youtube")
from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData

def determine_demonetized(videos,threshold):
    bad_videos = [];
    for video in videos:
        if video.percent < threshold:
            bad_videos.append(video)

    return bad_videos


m = YTAnalytics.Metrics()

days = 2
threshold = 0.1

youtube_edit_link = "https://www.youtube.com/edit?o=U&video_id="

# Setup APIs
api = GoogleAPIKey()
ytd = YTData()
ytd.set_client(api.get_client_id(),api.get_client_secret())

yta = YTAnalytics()
yta.set_client(api.get_client_id(),api.get_client_secret())

# Connect APIs
ytd.connect()
yta.connect()

ytd.set_channel_id(api.channel_id)
yta.set_channel_id(api.channel_id)

videos = ytd.get_video_list()


for video in videos:
    yta.get_metrics(
            date.today()-timedelta(days),
            date.today()-timedelta(1),
            [m.views,m.monetizedPlaybacks],
            video
    )

bad_videos = determine_demonetized(videos,threshold)

for bv in bad_videos:
    print("Video \"" + bv.title + "\" is at " + str(bv.percent*100) + "% monetized views") 
    print(youtube_edit_link + bv.id) 

