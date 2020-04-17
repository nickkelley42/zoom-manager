#!/usr/bin/env python3

import jwt
import config
from time import time
from math import floor

def get_jwt():
    return jwt.encode(
        {
            'iss': config.zoom_api_key,
            'exp': expiration()
        },
        config.zoom_api_secret,
        algorithm = 'HS256'
    )
    
def expiration():
    # 5 minutes from now
    return floor(time() + (5 * 60))

