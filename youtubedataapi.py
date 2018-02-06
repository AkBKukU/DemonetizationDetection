#!/usr/bin/python3

from googleapi import GoogleAPIBase


class YTData(GoogleAPIBase):

    channel_id = None


    def __init__(self):
        self.set_api(
                name = "youtube",
                version = "v3",
                scope = "https://www.googleapis.com/auth/youtube.force-ssl " + \
                    "https://www.googleapis.com/auth/youtube.readonly"
        )


    def set_channel_id(self,channel_id):
        self.channel_id = channel_id


    def get_video_list(self):
        result = self.service.videos().list(
                part="snippet"
            ).execute()
        video_ids = []
        for video in result.get("items", []):
            video_ids.append([ 
                video.get("id") ,
                video.get("snippet", []).get("title")
            ]) 
           
        return video_ids


