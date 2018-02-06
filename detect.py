#!/usr/bin/python3

from datetime import *
import sys
from pprint import *
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

videos = [ 
   [ "p5o6NQmEA-8","floppy","" ,[],[]],
   [ "GAk2YT8NwCc","changer","",[],[] ],
   [ "W3RhGGFiDt8","mic","" ,[],[]], 
   [ "C_XdrXjYqGE", "tek","",[],[] ]
]

for video in videos:
    for day in days:
        video[3].append(yta.get_views(date.today()-timedelta(day),video_id=video[0]))

for video in videos:
    for day in days:
        video[4].append(yta.get_monetizedPlaybacks(date.today()-timedelta(day),video_id=video[0]))

videos = [['p5o6NQmEA-8', 'floppy', '', [4.0, 3.0, 12.0], [2.0, 0.0, 0.0]],
         ['GAk2YT8NwCc', 'changer', '', [7.0, 12.0, 4.0], [6.0, 3.0, 4.0]],
          ['W3RhGGFiDt8', 'mic', '', [0.0, 77.0, 4.0], [0.0, 25.0, 3.0]],
           ['C_XdrXjYqGE', 'tek', '', [13.0, 11.0, 3.0], [0.0, 6.0, 0.0]]]



monetized_ratio(videos)

bad_videos = determine_demonetized(videos,threshold)

for bv in bad_videos:
    print("Video \"" + bv[1] + "\" is at " + str(bv[6]*100) + "% monetized views") 
    print(youtube_edit_link + bv[0]) 



#pprint(videos)

