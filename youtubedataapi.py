#!/usr/bin/python3

from googleapi import GoogleAPIBase

from pprint import *
from datetime import *

class YTData(GoogleAPIBase):

    channel_id = None


    def __init__(self):
        self.set_api(
                name = "youtube",
                version = "v3",
                scope = "https://www.googleapis.com/auth/youtube.force-ssl " + \
                    "https://www.googleapis.com/auth/youtube.readonly"
        )
        self.set_storage("./data_token.json")


    def set_channel_id(self,channel_id):
        self.channel_id = channel_id


    def get_video_list(self):
        end_of_videos = False
        video_ids = []
        timestamp = str(datetime.utcnow().replace(microsecond=0).isoformat())+"Z"
#        timestamp = "2011-07-10T20:35:40.000Z"
        max_results = 5
        max_loops = 10

        while not end_of_videos:
            max_loops = max_loops - 1
            result = self.service.search().list(
                    part="snippet",
                    channelId=self.channel_id,
                    maxResults=max_results,
                    order="date",
                    type='video',
                    publishedBefore = timestamp
                ).execute()

            for video in result.get("items", []):
                video_ids.append([ 
                    video.get("id").get("videoId") ,
                    video.get("snippet", []).get("title"),
                    video.get("snippet", []).get("publishedAt"),
                ])

            if len(result.get("items", [])) < max_results or max_loops == 0:
                end_of_videos = True
            else:
                timestamp = video_ids[-1][2]
                datestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
                datestamp = datestamp - timedelta(0,1)
                timestamp = str(datestamp.replace(microsecond=0).isoformat())+"Z"
                                
           
        return video_ids


