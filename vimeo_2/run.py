import vimeo

# The first step to interact with the API is to authorise by creating a client object

client = vimeo.Client(
  token='1433a10339f1ef1ce9f7996b75bb844d',
  key='112087199',
  secret='BXEJQCGEBXneJccdbsomEuyfQgJ6Z/6mf2r4f72EZN3laxEPw/I9QWuJdFkhvyJ7XmvYKh8fyPCwo2KhYl0Jw2kAGlf6kPJUdBMI64UhmtdJh2PEuOKd6lmXtpZPSKbe'
)

uri = 'https://api.vimeo.com/'

response = client.get(uri)
print (response.json())
