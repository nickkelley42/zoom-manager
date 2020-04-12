#!/usr/bin/env python3

import json
from sys import stdin

def get_form_data():
    data = json.load(stdin)
    return data
