#!/usr/bin/python3

out_of_project_files = "/home/akbkuku/.youtube/"

from youtubeanalyticsapi import YTAnalytics
sys.path.append(out_of_project_files)
from apikey import GoogleAPIKey

storage_file = out_of_project_files + "token.json"


# Connect to youtube api
api = GoogleAPIKey()
yt = YTAnalytics()
yt.set_channel_id(api.channel_id)
yt.set_client(api.client_id,api.client_secret)
yt.set_storage(storage_file)
yt.connect()


