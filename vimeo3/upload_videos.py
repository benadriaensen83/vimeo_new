import vimeo
from os import walk
import requests

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

  client.
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

directories, f = folder_file_names()

for item in f:
  print ('uploading video {}'.format(item))
  upload_video(item)

for item in directories:
