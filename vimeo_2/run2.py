import requests
import json
import pandas as pd

def fetch_all_videos():

    ## this method fetched all the videos uploaded on the user account

    # setup the variables for the API (Bearer token created in the browser)
    url = "https://api.vimeo.com/me/videos"

    payload = {}
    headers = {
      'Authorization': 'Bearer 1433a10339f1ef1ce9f7996b75bb844d'
    }

    # execute the call
    response = requests.request("GET", url, headers=headers, data = payload)

    # parse the response from to a dictionary for data handling
    response = response.json

    # print the response (using the json library to print a prettier layout)
    print(json.dumps(response, indent=4, sort_keys=True))

    return response

def get_video_details():

    ## this function obtains the video details (including the embed code)

    pass

data = fetch_all_videos()

data = pd.DataFrame(data)
print(data)

