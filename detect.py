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
        days_counter = days
        percents = []
        total = 0
        for x in range(0, days_counter-1):
            if video[3][x] > 0:
                ratio = video[4][x]/video[3][x]
                percents.append(ratio)
                total += ratio

            else:
                percents.append(0)

        video.append(percents)
        video.append(total/(days-1))


def determine_demonetized(videos,threshold):
    bad_videos = [];
    for video in videos:
        if video[6] < threshold:
            bad_videos.append(video)

    return bad_videos


api = GoogleAPIKey()
ytd = YTData()
ytd.set_channel_id(api.channel_id)
ytd.set_client(api.get_client_id(),api.get_client_secret())
ytd.connect()
ytd.get_video_list()

videos = ytd.get_video_list()


# Connect to youtube api
yta = YTAnalytics()
yta.set_channel_id(api.channel_id)
yta.set_client(api.get_client_id(),api.get_client_secret())
yta.connect()

for video in videos:
    video.append([])
    for day in list(reversed(range(1,days))):
        video[-1].append(yta.get_views(date.today()-timedelta(day),video_id=video[0]))

for video in videos:
    video.append([])
    for day in list(reversed(range(1,days))):
        video[-1].append(yta.get_monetizedPlaybacks(date.today()-timedelta(day),video_id=video[0]))


monetized_ratio(videos)

bad_videos = determine_demonetized(videos,threshold)

for bv in bad_videos:
    print("Video \"" + bv[1] + "\" is at " + str(bv[6]*100) + "% monetized views") 
    print(youtube_edit_link + bv[0]) 




