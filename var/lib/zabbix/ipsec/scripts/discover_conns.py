#!/usr/bin/env python

import json

data = []

conn = None
start = False

f = open('/etc/strongswan/ipsec.conf', 'r')
for line in f:
    line = line.strip()
    if line.find('conn', 0, 4) == 0:
        if conn is not None and start:
            conn['{#RTT_TIME_WARN}'] = '80'
            conn['{#RTT_TIME_ERR}'] = '150'
            data.append(conn)
        conn = { '{#TUNNEL}': line.split(' ', 2)[1].strip() }
        start = False
    elif conn is not None:
        option = line.split('=', 2)
        if len(option) == 2:
            key = option[0].strip()
            value = option[1].strip()
            if key == 'left':
                conn['{#SOURCEIP}'] = value
            elif key == 'right':
                conn['{#TARGETIP}'] = value
            elif key == 'auto' and value == 'start':
                start = True

if conn is not None and start:
    conn['{#RTT_TIME_WARN}'] = '80'
    conn['{#RTT_TIME_ERR}'] = '150'
    data.append(conn)

root = { 'data': data }
print json.dumps(root)