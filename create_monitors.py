#!/usr/bin/env python3

import argparse
import datadog
import os
import sys
import yaml

parser = argparse.ArgumentParser(
    description="Create new monitors in datadog based on local definitions"
)
parser.add_argument("filename", help="YAML file from which to read monitors")
args = parser.parse_args()

try:
    options = {"api_key": os.environ["DD_API_KEY"], "app_key": os.environ["DD_APP_KEY"]}
except KeyError:
    print(
        """You must set DD_API_KEY and DD_APP_KEY environment variables with
          API and Application keys for your Datadog account"""
    )
    print("See https://app.datadoghq.com/account/settings#api")
    sys.exit(1)

datadog.initialize(**options)

monitors = yaml.load(open(args.filename))
for monitor in monitors:
    datadog.api.Monitor.create(**monitor)
