import vimeo
from os import walk
import requests
import math

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

def folder_file_names():

  f = []
  for (dirpath, dirnames, filenames) in walk('upload_folder'):
    f.extend(filenames)
    break

  directories = []
  for item in f:
    directory = item.split(' ')[0]
    directories.append(directory)

  print('identified files are as follows:')
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

  print(response.text.encode('utf8'))

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

# script runs from here

# obtain a list of existing directories
# create a list instance
existing_dirs = []

# make the API call and calculate number of pages
data = obtain_all_folders()
total_pages = data['total']/data['per_page']
total_pages = total_pages
print(total_pages)

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




    # file name coding scheme is respected
    # list the files in the upload_folder, f lists the files, whereas directories is a list to generate directories (if the

# for item in directory_tags:
#
#   directory_tags, f = folder_file_names()
#
#   # upload each file
#   for item in f:
#     print('uploading video {}'.format(item))
#     upload_video(item)