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

    storage_file = "./token.json"

    client_id = None
    client_secret = None
    api_name = None
    api_version = None

    service = None

    credentials = None
    scopes = []

    def set_client(self, client_id, client_secret):
        GoogleAPIBase.client_id = client_id
        GoogleAPIBase.client_secret = client_secret

    def set_api(self, name, version):
        self.api_name = name
        self.api_version = version

    def set_storage(self, storage):
        self.storage_file = storage

    def add_scope(self, scope):
        GoogleAPIBase.scopes.append(scope)
        GoogleAPIBase.credentials = None

    def build_scope(self):
        scope = ""
        for s in GoogleAPIBase.scopes:
            scope += s + " "
        return scope

    def login(self):
        flow = OAuth2WebServerFlow(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.build_scope(),
            redirect_uri="http://localhost"
        )

        storage = Storage(self.storage_file)
        GoogleAPIBase.credentials = storage.get()

        if GoogleAPIBase.credentials is None or \
                GoogleAPIBase.credentials.invalid:
            flags = argparser.parse_args(args=[])
            GoogleAPIBase.credentials = run_flow(flow, storage, flags)

    def get_service(self):
        if GoogleAPIBase.credentials is None:
            self.login()
        return build(
            self.api_name, self.api_version,
            http=GoogleAPIBase.credentials.authorize(httplib2.Http()))

    def connect(self):
        self.service = self.get_service()

