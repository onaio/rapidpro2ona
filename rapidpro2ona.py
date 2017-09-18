#!/usr/bin/env python
import urlparse
import json
import requests
from config import TEST_DATA, ONA_FORM_ID, ONA_SUBMISSION_URL


def get_dict_from_rapidpro_data(data):
    """
    Returns a dict from RapidPro query string.
    """
    data_dict = urlparse.parse_qs(data)
    return data_dict


def ona_submission_json(data):
    submission_dict = dict()
    values = json.loads(data['values'][0])
    for value in values:
      submission_dict[value['label']] = value['text']
    return submission_dict


def post_to_ona_form(data, url=ONA_SUBMISSION_URL, id_string=ONA_FORM_ID):
    payload = {'id': id_string, 'submission': data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code in [201, 202]:
      return True
    
    return False


if __name__ == '__main__':
  data = get_dict_from_rapidpro_data(TEST_DATA)
  submission_data = ona_submission_json(data)
  if post_to_ona_form(submission_data):
    print 'Success'
  else:
    print 'Fail'
