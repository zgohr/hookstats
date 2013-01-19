#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from google.appengine.api import urlfetch

HEADERS = {
    'X-Parse-Application-Id': 'ElAH6C9vFmBLeO09O5qD0PgUfX0bA6v2zqiGap1L',
    'X-Parse-REST-API-Key': 'HmBjwglSnpTmzzGK3BRqtu5zD1LQndTbH8LJde1f',
    'Content-Type': 'application/json',
}


class GitstatsTestHandler(webapp2.RequestHandler):
    def post(self):
        data = self.request.body
        url = 'https://api.parse.com/1/classes/Push'
        result = urlfetch.fetch(url=url,
                                payload=data,
                                method=urlfetch.POST,
                                headers=HEADERS)
        self.response.write(result.content)

app = webapp2.WSGIApplication([
    ('/gitstats_test', GitstatsTestHandler)
], debug=True)
