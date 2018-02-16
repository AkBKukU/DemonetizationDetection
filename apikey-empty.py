#!/usr/bin/python3


class GoogleAPIKey():
    client_id = ""
    client_secret = ""
    channel_id = ""

    def set_client(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_channel_id(self):
        return self.client_id

    def get_client_id(self):
        return self.client_id

    def get_client_secret(self):
        return self.client_secret
