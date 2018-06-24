#!/usr/bin/env python3

# Compute auto extensions by talking directly with the server.
#
# Usage:
# To compute everyone's auto extensions:
#    $ python3 _compute_auto_ext.py > _auto_extensions.csv
#
# To compute an individual's:
#    $ python3 _compute_auto_ext.py USERNAME
# and manually update _auto_extensions.csv
#

# Information about progress will be printed to stderr so you can see it even
# when sending stdout to a file.

API_TOKEN = '99mEU06RYxe7Sj9xXFiFHEMNmgQiYfbCaOVJfnBzCF73In12y8NHManqOvauoXJGFI3GiC'
BASE_URL = 'https://iesc-s2.mit.edu/608'
COURSE = 'spring18'
PAGE = 'progress/get_week_delta'
MAX_WEEK = 9

import os
import sys
import json
import urllib.request, urllib.parse, urllib.error


if len(sys.argv) > 1:
    names = sys.argv[1:]
else:
    data = urllib.parse.urlencode({'api_token': API_TOKEN,
                                   'course': COURSE}).encode()
    request = urllib.request.Request(BASE_URL + '/cs_util/api/list_users', data)
    resp = urllib.request.urlopen(request, data).read().decode()
    names = sorted(json.loads(resp)['result'])

URL = '/'.join([BASE_URL, COURSE, PAGE])

#names = [name for name in names if name not in staff + done]

for name in names:
    overalls = {}
    oneweek = [None]*MAX_WEEK

    for w in range(1,MAX_WEEK):
        data = urllib.parse.urlencode({'api_token': API_TOKEN,
                                       'as': name,
                                       'week': str(w)}).encode()
        request = urllib.request.Request(URL, data)
        resp = urllib.request.urlopen(request, data).read().decode()
        s1, s2 = resp.strip().split()
        s1 = float(s1)
        s2 = float(s2)
        overalls[(w, w)] = s2
        oneweek[w] = s1
        print(name, w, s1, s2, file=sys.stderr)

    for i in range(1,MAX_WEEK):
        for j in range(i+1, MAX_WEEK):
            overalls[(i, j)] = oneweek[i] + oneweek[j]

    print('%s,%s,%s' % ((name,) + max(sorted(overalls), key=lambda x: overalls[x])))
