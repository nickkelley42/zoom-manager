#!/usr/bin/env python

import json

class Response:
    def __init__(self):
        self.content_type = "application/json"
        self.headers = []
        self.data = {}
        self.status = 200

    def send(self):
        print("Content-type: {}".format(self.content_type))
        print("Status:{}".format(self.status))
        for header in self.headers:
            print(header)
        print()
        print(json.dumps(self.data))

    def add_header(self, header):
        self.headers.append(header)
