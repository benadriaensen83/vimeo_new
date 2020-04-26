import vimeo
import os

def upload_video(file)

  # this method interacts with the API to upload the videos

  client = vimeo.VimeoClient(
    token='33d0604babd6ae462168c975cb25bd23',
    key='112087188',
    secret='BXEJQCGEBXneJccdbsomEuyfQgJ6Z/6mf2r4f72EZN3laxEPw/I9QWuJdFkhvyJ7XmvYKh8fyPCwo2KhYl0Jw2kAGlf6kPJUdBMI64UhmtdJh2PEuOKd6lmXtpZPSKbe'
  )

  file_name = 'upload_folder/dummy.mp4'
  uri = client.upload(file_name, data={
    'name': file,
    'description': 'The description goes here.'
  })

def folder_names():

