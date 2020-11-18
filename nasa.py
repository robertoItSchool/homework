# url: https://api.nasa.gov/planetary/apod
# call NASA with params api_key=DEMO_KEY, date of format YYYY-MM-DD (2019-03-20)
# Make a class with a method which makes the call and returns the tile and the explanation
# Write 3 tests for it which call the real API on different dates, can check only the title
# Write 3 tests which mock the API returning different titles and explanations

import requests

def get_today():
  response = requests.get('https://api.nasa.gov/planetary/apod',
                          params={'api_key': 'DEMO_KEY', 'date': '2020-11-18'})

  print(response)
  # get the content/data
  content = response.json()
  # get the title of the day
  title = content['title']
  print(title)

# get_today()

def get_month():
  i = 1
  while i < 30:
    date = '2020-08-' + str(i)
    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params={'api_key': 'DEMO_KEY', 'date': date})
    content = response.json()
    try:
      print(content['title'])
    except KeyError:
      print('no title for day ' + str(i))
      print(content['error']['code'])
    i += 1

get_month()