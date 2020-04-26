import pandas as pd
import requests
import json
import math


def fetch_all_videos_data(page_number=1):

    # this method fetched all the videos uploaded on the user account

    # setup the variables for the API (Bearer token created in the browser). The path parameter queries to show 100
    # results per page

    url = "https://api.vimeo.com/me/videos?per_page=100&page={}".format(page_number)

    payload = {}
    headers = {
      'Authorization': 'Bearer 1433a10339f1ef1ce9f7996b75bb844d'
    }

    # execute the call
    response = requests.request("GET", url, headers=headers, data = payload)

    # parse the response fro8m to a dictionary for data handling
    response = response.json

    return response

def fetch_total_page_numbers(response):

    # the data will be spread over multiple pages. First we need to identify how many, as given in the response.
    # we can achieve this by calculation of two data points and then rounding up
    number_pages = response['total']/response['per_page']

    # we round the number up to the next integer
    number_pages = math.ceil(number_pages)

    print('the number of pages is {}'.format(number_pages))

    return number_pages

def collect_and_structure_data(response, number_pages):


    # here we create a loop for each page number
    for i in range(number_pages):
        pass




data = fetch_all_videos_data()
total_pages = fetch_total_page_numbers(data)

# creates an empty list for data output

output = []

# here we create a loop to collect the data from all pages
for i in range(1, total_pages+1):
    print ('fetching page {}'.format(i))
    data = fetch_all_videos_data(page_number=i)

    data = data['data']

    for i in range(len(data)):
        entry= {'video_name': data[i]['name'],
         'video_uri': data[i]['uri'],
         'embed_link': data[i]['embed']['html']
         }

        output.append(entry)

# create dataframe for output and save to csv
output = pd.DataFrame (output)
output.to_csv('hyperlink_data.csv')
print(output)


