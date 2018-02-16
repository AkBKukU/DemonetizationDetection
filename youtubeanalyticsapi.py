#!/usr/bin/python3

import types
from pprint import pprint

from googleapi import GoogleAPIBase
from videodata import VideoData


class YTAnalytics(GoogleAPIBase):

    class Metrics:
        estimatedRevenue = "estimatedRevenue", \
            VideoData.estimatedRevenue
        estimatedMinutesWatched = "estimatedMinutesWatched", \
            VideoData.estimatedMinutesWatched
        monetizedPlaybacks = "monetizedPlaybacks", \
            VideoData.monetizedPlaybacks
        views = "views", \
            VideoData.views

    def __init__(self):
        self.set_api("youtubeAnalytics","v1")
        self.add_scope("https://www.googleapis.com/auth/yt-analytics.readonly")
        self.add_scope("https://www.googleapis.com/auth/yt-analytics-monetary.readonly")
        self.m = self.Metrics()

    def set_channel_id(self, channel_id):
        self.channel_id = channel_id

    def execute_query(self, start, end, metrics, video=None):
        if video:
            filters = "video==" + video.id
        else:
            filters = ""

        return self.service.reports().query(
            ids="channel=="+self.channel_id,
            filters=filters,
            metrics=metrics,
            start_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
        ).execute()

    def get_metrics(self, start, end, metrics, video):
        if end is None:
            end = start

        metricString = ""
        for m in metrics:
            metricString += m[0] + ","

        metricString = metricString[:-1]

        result = self.execute_query(start, end, metricString, video)

        for row in result.get("rows",  []):
            for i, value in enumerate(row):
                types.MethodType(metrics[i][1].fset, video)(value)

        return video

