#!/usr/bin/python3

import sys
from datetime import *
from pprint import *

from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData

views_for_confidence = 25
days = 4
threshold = 0.1


def determine_demonetized(videos, threshold):
    bad_videos = [[], [], []]
    for video in videos:
        if video.percent < threshold:
            if video.percent_confidence > 1.0:
                bad_videos[0].append(video)
            elif video.percent_confidence > 0.5:
                bad_videos[1].append(video)
            else:
                bad_videos[2].append(video)
    return bad_videos


def print_video(video):
        print('Video "%s" is at %d%% (%d/%d) monetized views' % (
            video.title,
            video.percent*100,
            video.monetizedPlaybacks,
            video.views
        ))
        print(youtube_edit_link + video.id)


m = YTAnalytics.Metrics()
VideoData.percent_confidence_limit = views_for_confidence
youtube_edit_link = "https://www.youtube.com/edit?o=U&video_id="

# Setup APIs
api = GoogleAPIKey()
ytd = YTData()
ytd.set_client(api.get_client_id(), api.get_client_secret())
ytd.set_channel_id(api.channel_id)

yta = YTAnalytics()
yta.set_client(api.get_client_id(), api.get_client_secret())
yta.set_channel_id(api.channel_id)

# Connect APIs
ytd.connect()
yta.connect()

# Get all videos
videos = ytd.get_video_list()

for video in videos:
    yta.get_metrics(
            date.today()-timedelta(days),
            date.today()-timedelta(1),
            [m.views, m.monetizedPlaybacks],
            video
    )

bad_videos = determine_demonetized(videos, threshold)

if len(bad_videos[0]):
    print("High Confidence of Demonetiztion:")
    for bv in bad_videos[0]:
        print_video(bv)
    print()

if len(bad_videos[1]):
    print("Medium Confidence of Demonetiztion:")
    for bv in bad_videos[1]:
        print_video(bv)
    print()

if len(bad_videos[2]):
    print("Low Confidence of Demonetiztion:")
    for bv in bad_videos[2]:
        print_video(bv)
    print()

