#!/usr/bin/python3

from googleapi import GoogleAPIBase


class YTAnalytics(GoogleAPIBase):

    class Metrics:
        estimatedRevenue = "estimatedRevenue"
        estimatedMinutesWatched="estimatedMinutesWatched"
        monetizedPlaybacks = "monetizedPlaybacks"
        views = "views"

    m  = None

    channel_id = None


    def __init__(self):
        self.set_api(
                name = "youtubeAnalytics",
                version = "v1",
        )
        self.add_scope("https://www.googleapis.com/auth/yt-analytics.readonly")
        self.add_scope("https://www.googleapis.com/auth/yt-analytics-monetary.readonly")
        self.m = self.Metrics() 


    def set_channel_id(self,channel_id):
        self.channel_id = channel_id


    def execute_query(self,start,end,metrics,video_id=None):
        if video_id == None:
            filters = ""
        else:
            filters = "video==" + video_id

        return self.service.reports().query(
            ids="channel=="+self.channel_id,
            filters=filters,
            metrics=metrics,
            start_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
            ).execute()

    def get_monetizedPlaybacks(self,start,end=None,video_id=None):
        if end == None:
            end = start

        result = self.execute_query(start,end,self.m.monetizedPlaybacks,video_id)

        for row in result.get("rows", []):
            for value in row:
                return value

        return -1


    def get_views(self,start,end=None,video_id=None):
        if end == None:
            end = start

        result = self.execute_query(start,end,self.m.views,video_id)

        for row in result.get("rows", []):
            for value in row:
                return value

        return -1


    def get_revenue(self,start,end=None,video_id=None):
        if end == None:
            end = start

        result = self.execute_query(start,end,self.m.estimatedRevenue,video_id)

        for row in result.get("rows", []):
            for value in row:
                return value

        return -1


    def get_watchtime(self,start,end=None):
        if end == None:
            end = start

        result = self.execute_query(start,end,self.m.estimatedMinutesWatched)

        for row in result.get("rows", []):
            for value in row:
                return value / 60.0

        return -1

