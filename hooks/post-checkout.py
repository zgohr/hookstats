#! /usr/bin/env python

import sys
import subprocess
import json
import httplib

POST_HEADERS = {
    'X-Parse-Application-Id': '',
    'X-Parse-REST-API-Key': '',
    'Content-Type': 'application/json',
}


def git(args):
    args = ['git'] + args
    git = subprocess.Popen(args, stdout=subprocess.PIPE)
    details = git.stdout.read().strip()
    return details


def post(data):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/Checkout', json.dumps(data),
                       POST_HEADERS
                       )
    return json.loads(connection.getresponse().read())


def get_remotes():
    remotes = []
    git_list = git(['remote', '-v']).split('\n')
    for remote in git_list:
        name, command = remote.split('\t')
        url, command = command.split(' ')
        if command == '(push)':
            remotes.append(url)
    return remotes


def build_payload():
    payload = {
        'branch_name': git(['rev-parse', '--abbrev-ref', 'HEAD']),
        'user_email': git(['config', 'user.email']),
        'remotes': [] + get_remotes(),
    }
    return payload


if __name__ == '__main__':
    command, from_hash, to_hash, checkout_type = sys.argv
    if int(checkout_type) is not 1:
        sys.exit(0)
    post(build_payload())
    sys.exit(1)
