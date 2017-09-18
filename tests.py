import unittest
from rapidpro2ona import get_dict_from_rapidpro_data
from rapidpro2ona import ona_submission_json

response_string = 'run=74602&text=0&flow_uuid=f1d17e8c-19de-4365-810a-34fa606c05b1&phone=%2B12065550100&step=RuleSet%3A+cce7a27a-251c-43fd-aedc-b3063942d9a7+-+results&contact_name=Antonate+Maritim&flow_name=Service+mapping&header=Authorization&urn=tel%3A%2B12065550100&flow=1002&relayer=-1&contact=fe4df540-39c1-4647-b4bc-1c93833e22e0&values=%5B%7B%22category%22%3A+%7B%22base%22%3A+%22name%22%7D%2C+%22node%22%3A+%227b6d52a2-c17a-45f8-8d0a-8ddd1ad102d3%22%2C+%22time%22%3A+%222017-09-15T11%3A55%3A40.552881Z%22%2C+%22text%22%3A+%22nate%22%2C+%22rule_value%22%3A+%22nate%22%2C+%22value%22%3A+%22nate%22%2C+%22label%22%3A+%22name%22%7D%2C+%7B%22category%22%3A+%7B%22base%22%3A+%221+-+120%22%7D%2C+%22node%22%3A+%22cfe03a9a-2903-4112-94a5-b176cccc8691%22%2C+%22time%22%3A+%222017-09-15T11%3A55%3A42.374803Z%22%2C+%22text%22%3A+%2222%22%2C+%22rule_value%22%3A+%2222%22%2C+%22value%22%3A+%2222.00000000%22%2C+%22label%22%3A+%22age%22%7D%2C+%7B%22category%22%3A+%7B%22base%22%3A+%22Female%22%7D%2C+%22node%22%3A+%22c1567c75-387d-434f-a882-0de45deb9a33%22%2C+%22time%22%3A+%222017-09-15T11%3A55%3A45.810629Z%22%2C+%22text%22%3A+%22female%22%2C+%22rule_value%22%3A+%22female%22%2C+%22value%22%3A+%22female%22%2C+%22label%22%3A+%22gender%22%7D%2C+%7B%22category%22%3A+%7B%22base%22%3A+%220%22%7D%2C+%22node%22%3A+%2243c255ee-eb40-4c92-9e62-5b9252e944af%22%2C+%22time%22%3A+%222017-09-15T11%3A55%3A49.015773Z%22%2C+%22text%22%3A+%220%22%2C+%22rule_value%22%3A+%220%22%2C+%22value%22%3A+%220E-8%22%2C+%22label%22%3A+%22no_children%22%7D%5D&time=2017-09-15T11%3A55%3A49.056905Z&steps=%5B%7B%22node%22%3A+%22aa017ff6-d8cc-486c-ae5f-652d29892aad%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A37.680459Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A37.757281Z%22%2C+%22text%22%3A+%22What+is+your+name%3F%22%2C+%22type%22%3A+%22A%22%2C+%22value%22%3A+null%7D%2C+%7B%22node%22%3A+%227b6d52a2-c17a-45f8-8d0a-8ddd1ad102d3%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A37.757281Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A40.552881Z%22%2C+%22text%22%3A+%22nate%22%2C+%22type%22%3A+%22R%22%2C+%22value%22%3A+%22nate%22%7D%2C+%7B%22node%22%3A+%22e6672744-a629-4ecd-b9ba-d21d1c19ad99%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A40.552881Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A40.625965Z%22%2C+%22text%22%3A+%22What+is+your+age%3F%22%2C+%22type%22%3A+%22A%22%2C+%22value%22%3A+null%7D%2C+%7B%22node%22%3A+%22cfe03a9a-2903-4112-94a5-b176cccc8691%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A40.625965Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A42.374803Z%22%2C+%22text%22%3A+%2222%22%2C+%22type%22%3A+%22R%22%2C+%22value%22%3A+%2222%22%7D%2C+%7B%22node%22%3A+%227063d9ea-d051-4826-bd45-269aaa7de527%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A42.374803Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A42.434251Z%22%2C+%22text%22%3A+%22What+is+your+gender%3F+Answer+with+female+or+male%22%2C+%22type%22%3A+%22A%22%2C+%22value%22%3A+null%7D%2C+%7B%22node%22%3A+%22c1567c75-387d-434f-a882-0de45deb9a33%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A42.434251Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A45.810629Z%22%2C+%22text%22%3A+%22female%22%2C+%22type%22%3A+%22R%22%2C+%22value%22%3A+%22female%22%7D%2C+%7B%22node%22%3A+%22d7134b54-346b-4d9e-96c3-1d6997cb5b12%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A45.810629Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A45.885510Z%22%2C+%22text%22%3A+%22How+many+children+do+you+have%3F%22%2C+%22type%22%3A+%22A%22%2C+%22value%22%3A+null%7D%2C+%7B%22node%22%3A+%2243c255ee-eb40-4c92-9e62-5b9252e944af%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A45.885510Z%22%2C+%22left_on%22%3A+%222017-09-15T11%3A55%3A49.015773Z%22%2C+%22text%22%3A+%220%22%2C+%22type%22%3A+%22R%22%2C+%22value%22%3A+%220%22%7D%2C+%7B%22node%22%3A+%22cce7a27a-251c-43fd-aedc-b3063942d9a7%22%2C+%22arrived_on%22%3A+%222017-09-15T11%3A55%3A49.015773Z%22%2C+%22left_on%22%3A+null%2C+%22text%22%3A+null%2C+%22type%22%3A+%22R%22%2C+%22value%22%3A+null%7D%5D&flow_base_language=base&channel=-1'

expected_data = {'flow_name': ['Service mapping'], 'run': ['74602'], 'header': ['Authorization'], 'text': ['0'], 'urn': ['tel:+12065550100'], 'flow': ['1002'], 'phone': ['+12065550100'], 'flow_uuid': ['f1d17e8c-19de-4365-810a-34fa606c05b1'], 'relayer': ['-1'], 'step': ['RuleSet: cce7a27a-251c-43fd-aedc-b3063942d9a7 - results'], 'contact': ['fe4df540-39c1-4647-b4bc-1c93833e22e0'], 'values': ['[{"category": {"base": "name"}, "node": "7b6d52a2-c17a-45f8-8d0a-8ddd1ad102d3", "time": "2017-09-15T11:55:40.552881Z", "text": "nate", "rule_value": "nate", "value": "nate", "label": "name"}, {"category": {"base": "1 - 120"}, "node": "cfe03a9a-2903-4112-94a5-b176cccc8691", "time": "2017-09-15T11:55:42.374803Z", "text": "22", "rule_value": "22", "value": "22.00000000", "label": "age"}, {"category": {"base": "Female"}, "node": "c1567c75-387d-434f-a882-0de45deb9a33", "time": "2017-09-15T11:55:45.810629Z", "text": "female", "rule_value": "female", "value": "female", "label": "gender"}, {"category": {"base": "0"}, "node": "43c255ee-eb40-4c92-9e62-5b9252e944af", "time": "2017-09-15T11:55:49.015773Z", "text": "0", "rule_value": "0", "value": "0E-8", "label": "no_children"}]'], 'time': ['2017-09-15T11:55:49.056905Z'], 'steps': [
    '[{"node": "aa017ff6-d8cc-486c-ae5f-652d29892aad", "arrived_on": "2017-09-15T11:55:37.680459Z", "left_on": "2017-09-15T11:55:37.757281Z", "text": "What is your name?", "type": "A", "value": null}, {"node": "7b6d52a2-c17a-45f8-8d0a-8ddd1ad102d3", "arrived_on": "2017-09-15T11:55:37.757281Z", "left_on": "2017-09-15T11:55:40.552881Z", "text": "nate", "type": "R", "value": "nate"}, {"node": "e6672744-a629-4ecd-b9ba-d21d1c19ad99", "arrived_on": "2017-09-15T11:55:40.552881Z", "left_on": "2017-09-15T11:55:40.625965Z", "text": "What is your age?", "type": "A", "value": null}, {"node": "cfe03a9a-2903-4112-94a5-b176cccc8691", "arrived_on": "2017-09-15T11:55:40.625965Z", "left_on": "2017-09-15T11:55:42.374803Z", "text": "22", "type": "R", "value": "22"}, {"node": "7063d9ea-d051-4826-bd45-269aaa7de527", "arrived_on": "2017-09-15T11:55:42.374803Z", "left_on": "2017-09-15T11:55:42.434251Z", "text": "What is your gender? Answer with female or male", "type": "A", "value": null}, {"node": "c1567c75-387d-434f-a882-0de45deb9a33", "arrived_on": "2017-09-15T11:55:42.434251Z", "left_on": "2017-09-15T11:55:45.810629Z", "text": "female", "type": "R", "value": "female"}, {"node": "d7134b54-346b-4d9e-96c3-1d6997cb5b12", "arrived_on": "2017-09-15T11:55:45.810629Z", "left_on": "2017-09-15T11:55:45.885510Z", "text": "How many children do you have?", "type": "A", "value": null}, {"node": "43c255ee-eb40-4c92-9e62-5b9252e944af", "arrived_on": "2017-09-15T11:55:45.885510Z", "left_on": "2017-09-15T11:55:49.015773Z", "text": "0", "type": "R", "value": "0"}, {"node": "cce7a27a-251c-43fd-aedc-b3063942d9a7", "arrived_on": "2017-09-15T11:55:49.015773Z", "left_on": null, "text": null, "type": "R", "value": null}]'], 'contact_name': ['Antonate Maritim'], 'flow_base_language': ['base'], 'channel': ['-1']}


class TestRapidpro2Ona(unittest.TestCase):
  def test_get_dict_from_rapidpro_data(self):
    data = get_dict_from_rapidpro_data(response_string)
    self.assertEqual(data, expected_data)

  def test_ona_submission_json(self):
    data = get_dict_from_rapidpro_data(response_string)
    data_dict = ona_submission_json(data)
    expected_data = {u'gender': u'female', u'age': u'22',
                      u'name': u'nate', u'no_children': u'0'}
    self.assertEqual(data_dict, expected_data)
