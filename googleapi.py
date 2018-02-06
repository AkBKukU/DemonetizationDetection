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

class GoogleAPIBase():
    api_name = None
    api_version = None

    scope = None

    storage_file = "./token.json"

    client_id = None
    client_secret = None
    
    service = None

    def set_client(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def set_api(self,name,version,scope):
        self.api_name = name
        self.api_version = version
        self.scope = scope
    
    def set_storage(self,storage):
        self.storage_file = storage

    def get_service(self):
        flow = OAuth2WebServerFlow(client_id=self.client_id,
            client_secret=self.client_secret,           
            scope=self.scope,
            redirect_uri="http://localhost"
        )

        storage = Storage(self.storage_file)

        credentials = storage.get()

        if credentials is None or credentials.invalid:
            flags = argparser.parse_args(args=[])
            credentials = run_flow(flow, storage, flags)

        return build(self.api_name,self.api_version,
            http=credentials.authorize(httplib2.Http()))

    def connect(self):
        self.service = self.get_service()

