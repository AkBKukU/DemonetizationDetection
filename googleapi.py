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
    scopes = []

    storage_file = "./token.json"

    client_id = None
    client_secret = None
    
    service = None

    credentials = None

    def set_client(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def set_api(self,name,version,scope):
        self.api_name = name
        self.api_version = version
    
    def set_storage(self,storage):
        self.storage_file = storage

    def add_scope(self,scope):
        scopes.append(scope)

    def build_scope(self):
        scope = ""
        for s in self.scopes:
            scope += s + " "
        
        return scope

    def login(self):
        flow = OAuth2WebServerFlow(client_id=self.client_id,
            client_secret=self.client_secret,           
            scope=self.build_scope,
            redirect_uri="http://localhost"
        )

        storage = Storage(self.storage_file)

        self.credentials = storage.get()

        if self.credentials is None or self.credentials.invalid:
            flags = argparser.parse_args(args=[])
            self.credentials = run_flow(flow, storage, flags)

    def get_service(self,name,version):
        if not self.credentials:
            self.login()
        else:
            return build(name,version,
                http=self.credentials.authorize(httplib2.Http()))

    def connect(self):
        self.service = self.get_service()

