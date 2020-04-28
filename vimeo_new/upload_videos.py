import vimeo
from os import walk
import requests
import math
import pandas as pd
from tqdm import tqdm
import fetch_data

def upload_video(file):

  # this method interacts with the API to upload the videos
  client = vimeo.VimeoClient(
    token='33d0604babd6ae462168c975cb25bd23',
    key='112087188',
    secret='BXEJQCGEBXneJccdbsomEuyfQgJ6Z/6mf2r4f72EZN3laxEPw/I9QWuJdFkhvyJ7XmvYKh8fyPCwo2KhYl0Jw2kAGlf6kPJUdBMI64UhmtdJh2PEuOKd6lmXtpZPSKbe'
  )

  file_name = 'upload_folder/{}'.format(file)
  uri = client.upload(file_name, data={
    'name': file,
    'description': 'The description goes here.'
  })
  return uri

def folder_file_names():

  f = []
  for (dirpath, dirnames, filenames) in walk('upload_folder'):
    f.extend(filenames)
    break

  directories = []
  for item in f:
    directory = item.split(' ')[0]
    directories.append(directory)

  print('identified files for upload are as follows:')
  print(f)


  print('unique folder names are:')
  directories = list(set(directories))
  print(directories)

  return directories, f

def create_vimeo_folder(name):

  url = "https://api.vimeo.com/me/projects?user_id=112087188"

  payload = 'name={}'.format(name)
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'name': '\'jef\'',
    'Authorization': 'Bearer 7256c4503a4dc9229c8c68336c7f1932'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return

def obtain_all_folders(page_number=1):

  url = "https://api.vimeo.com/me/projects?per_page=100&page={}".format(page_number)

  payload = {}
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'name': '\'jef\'',
    'Authorization': 'Bearer 7256c4503a4dc9229c8c68336c7f1932'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  response = response.json()

  return response

def move_file_to_dir(folder_id, video_id):
  url = "https://api.vimeo.com/me/projects/{}/videos/{}".format(folder_id, video_id)

  payload = {}
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer 7256c4503a4dc9229c8c68336c7f1932'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  return response

  pass

def main():

  # obtain a list of existing directories
  # create a list instance
  existing_dirs = []

  # make the API call and calculate number of pages
  data = obtain_all_folders()
  total_pages = data['total']/data['per_page']
  total_pages = total_pages

  # we round the number up to the next integer (this changes the object type from Float to int)
  number_pages = math.ceil(total_pages)
  print('the total number of pages containing directory names = {}'.format(number_pages))

  # loop through each page to collect the data and append to the list of existing dirs
  for i in range(1, number_pages+1):
      print('fetching page {}'.format(i))
      data = obtain_all_folders(page_number=i)
      data = data['data']
      for item in data:
        entry = item['name']
        existing_dirs.append(entry)

  print ('the list of existing dirs looks as follows')
  print(existing_dirs)

  # list the files in the upload_folder, f lists the files, whereas directories is a list to generate directories (if the
  # file name coding scheme is respected

  directory_tags, f = folder_file_names()

  # here we check whether the directory tags are already in the list of existing directories. If not, we'll create them
  for tag in directory_tags:
    if tag not in existing_dirs:
      create_vimeo_folder(tag)

  # first, we upload the files to vimeo, then we'll assign them to the folders. We identify a list of existing files, to
  # avoid duplicate uploads. We can easily copy the script from the fetch_data.py script
  existing_files = fetch_data.collect_video_data()

  # we create a list to populate with all of the filenames
  existing_files_names = []

  for item in existing_files:
    entry = item['video_name']
    existing_files_names.append(entry)

  print('existing files names are')
  print(existing_files_names)

  uploaded_videos = []

  # let's make a progress bar for uploading files with tqdm
  print('executing uploads')
  for item in tqdm(f):
    if not item in existing_files_names:
      print('uploading video {}'.format(item))
      data = upload_video(item)
      entry = {'video_id': data.rsplit('/')[-1], 'video_name':item, 'video_dir_to_be': item.split(' ')[0]}
      uploaded_videos.append(entry)
    else:
      print('file {} not uploaded, as it already exists on vimeo platform'.format(item))

  # now we have to rearrange our uploaded files into the created directories. for that, we need the folder and file IDs
  existing_dirs = []
  data = obtain_all_folders()
  total_pages = data['total'] / data['per_page']
  total_pages = total_pages

  # we round the number up to the next integer (this changes the object type from Float to int)
  number_pages = math.ceil(total_pages)
  print('the total number of pages containing directory names = {}'.format(number_pages))

  # here we list the existing video directories again, after the new ones were added (if applicable)
  for i in range(1, number_pages+1):
      print('fetching page {}'.format(i))
      data = obtain_all_folders(page_number=i)
      data = data['data']
      for item in data:
        entry = {'name': item['name'], 'folder_id' : item['uri'].rsplit('/')[-1]}
        existing_dirs.append(entry)

  print('the list of existing directories on the Vimeo platform is as follows:')
  print(existing_dirs)
  print('the list of updated videos looks like this:')
  print(uploaded_videos)

  for item in uploaded_videos:
    for entry in existing_dirs:
      if item['video_dir_to_be'] == entry['name']:
        move_file_to_dir(entry['folder_id'], item['video_id'])

  output = fetch_data.collect_video_data()
  # create dataframe for output and save to csv
  output = pd.DataFrame(output)
  output.to_csv('hyperlink_data.csv')
  print(output)

  return

if __name__ == '__main__':
    main()
