#!/usr/bin/python3

from googleapi import GoogleAPIBase
from videodata import VideoData

from datetime import *
import math


class YTData(GoogleAPIBase):

    channel_id = None

    def __init__(self):
        self.set_api("youtube", "v3")
        self.add_scope("https://www.googleapis.com/auth/youtube.force-ssl")
        self.add_scope("https://www.googleapis.com/auth/youtube.readonly")

    def set_channel_id(self, channel_id):
        self.channel_id = channel_id

    def get_video_list(self, limit=0):
        max_loops = 50
        max_results = 50
        if limit:
            max_loops = math.floor(limit / 50)
            max_results = limit % 50

        end_of_videos = False
        videos = []
        timestamp = str(datetime.utcnow().replace(microsecond=0).isoformat()) \
            + "Z"

        while not end_of_videos:
            result_limit = max_results if not max_loops else 50
            result = self.service.search().list(
                    part="snippet",
                    channelId=self.channel_id,
                    maxResults=result_limit,
                    order="date",
                    type='video',
                    publishedBefore = timestamp
                ).execute()

            for video in result.get("items", []):
                videos.append(VideoData())
                videos[-1].id = video.get("id").get("videoId")
                snippet = video.get("snippet", [])
                videos[-1].title = snippet.get("title")
                videos[-1].published = snippet.get("publishedAt")

            # Loop End
            max_loops = max_loops - 1
            if len(result.get("items", [])) < max_results or max_loops < 0:
                end_of_videos = True
            else:
                timestamp = videos[-1].published
                datestamp = datetime.strptime(
                        timestamp, "%Y-%m-%dT%H:%M:%S.%fZ"
                )
                datestamp = datestamp - timedelta(0, 1)
                timestamp = str(datestamp.replace(microsecond=0).isoformat()) \
                    + "Z"

        return videos


