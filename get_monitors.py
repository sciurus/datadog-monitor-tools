#!/usr/bin/env python3

import argparse
import datadog
import os
import sys
import yaml

parser = argparse.ArgumentParser(description='Download monitors from datadog')
parser.add_argument('--name', dest='name', default='',
                    help='A string to filter monitors by name')
parser.add_argument('--tags', dest='tags', default=None,
                    help='''A comma separated list indicating what tags should
                         be used to filter the list of monitors by scope''')
parser.add_argument('--monitor-tags', dest='monitor_tags', default=None,
                    help='''A comma separated list indicating what service or
                         custom tags should be used to filter the list of monitors''')
args = vars(parser.parse_args())

try:
    options = {
        'api_key': os.environ['DD_API_KEY'],
        'app_key': os.environ['DD_APP_KEY'],
    }
except KeyError:
    print('''You must set DD_API_KEY and DD_APP_KEY environment variables with
          API and Application keys for your Datadog account''')
    print('See https://app.datadoghq.com/account/settings#api')
    sys.exit(1)

datadog.initialize(**options)


raw_monitors = datadog.api.Monitor.get_all(**args)

monitors = [{'id': m['id'], 'name': m['name'], 'query': m['query'],
             'message': m['message'], 'options': m['options'],
             'tags': m['tags']} for m in raw_monitors]

print(yaml.dump(monitors))
