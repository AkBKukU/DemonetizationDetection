#!/usr/bin/python3

from googleapi import GoogleAPIBase


class YTAnalytics(GoogleAPIBase):

    class Metrics:
        estimatedMinutesWatched="estimatedMinutesWatched"

    m  = None

    channel_id = None


    def __init__(self):
        self.set_api(
                name = "youtubeAnalytics",
                version = "v1",
                scope = "https://www.googleapis.com/auth/yt-analytics.readonly"
        )
        self.m = self.Metrics()


    def set_channel_id(self,channel_id):
        self.channel_id = channel_id


    def execute_query(self,start,end,metrics):
        return self.service.reports().query(
            ids="channel=="+self.channel_id,
            metrics=metrics,
            start_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
            ).execute()


    def get_watchtime(self,start,end=None):
        if end == None:
            end = start

        result = self.execute_query(start,end,self.m.estimatedMinutesWatched)

        for row in result.get("rows", []):
            for value in row:
                return value / 60.0

        return -1

