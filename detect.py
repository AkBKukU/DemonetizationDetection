#!/usr/bin/python3

import sys
from datetime import *
from pprint import *

# My test data
#from data import videos

out_of_project_files = "/home/akbkuku/.youtube/"

sys.path.append("/home/akbkuku/.youtube")
from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey

days = 4
threshold = 0.1

youtube_edit_link = "https://www.youtube.com/edit?o=U&video_id="


def monetized_ratio(videos):
    for video in videos:
        video.percent = video.monetizedPlaybacks/video.views


def determine_demonetized(videos,threshold):
    bad_videos = [];
    for video in videos:
        if video.percent < threshold:
            bad_videos.append(video)

    return bad_videos

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

videos = ytd.get_video_list()
#videos = [["dFnvu3tRLoo","SOBAX",""]]


# Connect to youtube api
yta.set_channel_id(api.channel_id)

#for video in videos:
#    pprint(yta.execute_query(date.today()-timedelta(days),date.today()-timedelta(1),"views,monetizedPlaybacks",video_id=video.video_id))

for video in videos:
    video.views = yta.get_views(date.today()-timedelta(days),date.today()-timedelta(1),video_id=video.video_id)

for video in videos:
    video.monetizedPlaybacks = yta.get_monetizedPlaybacks(date.today()-timedelta(days),date.today()-timedelta(1),video_id=video.video_id)


monetized_ratio(videos)

bad_videos = determine_demonetized(videos,threshold)


#for video in videos:
#    print(vars(video))

for bv in bad_videos:
    print("Video \"" + bv.title + "\" is at " + str(bv.percent*100) + "% monetized views") 
    print(youtube_edit_link + bv.video_id) 




