import os
import json
import requests
import config

def compiler(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(requests.post(
        post_url,
        json={
            "script": f"{code}",
            "language": "python3",
            "versionIndex": "3",
            "clientId": "620f757cc9063781eed92d9dcd8adf10",
            "clientSecret": "c449f16dcf817e17b74faaab4c46e5b4aac768a57c67f102b64b5054ca0c4c8b"
        }
    ).content)