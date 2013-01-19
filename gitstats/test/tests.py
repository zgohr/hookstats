import unittest
import json
import httplib

with open('../config/global.json') as f:
    config = json.load(f)

APPLICATION_ID = config['applications']['gitstats_test']['applicationId']
API_KEY = config['applications']['gitstats_test']['restKey']
POST_HEADERS = {
    'X-Parse-Application-Id': APPLICATION_ID,
    'X-Parse-REST-API-Key': API_KEY,
    'Content-Type': 'application/json',
}


def post(data, verb, resource_type, resource_name):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request(verb, '/'.join(['/1', resource_type, resource_name,]),
                       json.dumps(data),
                       POST_HEADERS)
    response = connection.getresponse().read()
    return json.loads(response)


class TestFunctions(unittest.TestCase):
    def test_trivial(self):
        data = {'success': 'yes'}
        result = post(data, 'POST', 'functions', 'trivial')
        self.assertEqual(result['result'], data)


if __name__ == "__main__":
    unittest.main()
