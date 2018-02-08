#!/usr/bin/python3

# python
import http.client
import httplib2
import os
import random
import sys
import time
import webbrowser
import threading
import pprint

# google
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow 
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

sys.path.append("/home/akbkuku/.youtube")
from apikey import GoogleAPIKey

api = GoogleAPIKey()
flow = OAuth2WebServerFlow(client_id=api.client_id,
    client_secret=api.client_secret,           
    scope="https://www.googleapis.com/auth/yt-analytics.readonly " + \
        "https://www.googleapis.com/auth/yt-analytics-monetary.readonly " + \
        "https://www.googleapis.com/auth/youtube.force-ssl " + \
        "https://www.googleapis.com/auth/youtube.readonly",
    redirect_uri="http://localhost"
)

storage = Storage("./aio_token.json")

credentials = storage.get()

if credentials is None or credentials.invalid:
    flags = argparser.parse_args(args=[])
    credentials = run_flow(flow, storage, flags)

ytd = build("youtube","v3", http=credentials.authorize(httplib2.Http()))
yta = build("youtubeAnalytics","v1", http=credentials.authorize(httplib2.Http()))



