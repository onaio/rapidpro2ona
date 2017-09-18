#! /usr/bin/python
import urlparse
import json
import requests

def get_dict_from_rapidpro_data(data):
  data_dict = urlparse.parse_qs(data)
  return data_dict

# data = get_dict_from_rapidpro_data(response_string)
# print data

def ona_submission_json(data):
  submission_dict = dict()
  values = json.loads(data['values'][0])
  for value in values:
    submission_dict[value['label']] = value['text']

  return submission_dict

# submission_dict = ona_submission_json(data)
# print submission_dict

# url = 'http://localhost:8000/nate/submission'
# payload = {'id': 'rapidpro_example', 'submission': submission_dict}
# headers = {'Content-Type: application/json',
#            'Authorization: Token 0388df853306ce9d845b94b81f29a6ef29c9f679'}
# res = requests.post(url, data=payload, headers=headers)
# print res

# curl - H "Content-Type: application/json" - H "Authorization: Token 0388df853306ce9d845b94b81f29a6ef29c9f679" - X POST "http://localhost:8000/nate/submission" - d '{"id":"rapidpro_example","submission":{"gender": "female", "age": "23", "name": "nate", "no_children": "0"}}'
