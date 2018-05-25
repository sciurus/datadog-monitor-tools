#!/usr/bin/env python3

import argparse
import datadog
import os
import sys
import yaml


def output_monitor(full_monitor, purpose):
    monitor = {
        "name": full_monitor["name"],
        "query": full_monitor["query"],
        "message": full_monitor["message"],
        "options": full_monitor["options"],
        "tags": full_monitor["tags"],
    }
    if purpose == "update":
        monitor["id"] = full_monitor["id"]
    else:
        monitor["type"] = full_monitor["type"]
    return monitor


parser = argparse.ArgumentParser(description="Download monitors from datadog")
parser.add_argument(
    "--name", dest="name", default="", help="A string to filter monitors by name"
)
parser.add_argument(
    "--purpose",
    dest="purpose",
    default="update",
    choices=["update", "create"],
    help="Choose if output is sutitable for updating existing monitors or creating new ones. Defaults to 'update'",
)
parser.add_argument(
    "--tags",
    dest="tags",
    default=None,
    help="A comma separated list indicating what tags should be used to filter the list of monitors by scope",
)
parser.add_argument(
    "--monitor-tags",
    dest="monitor_tags",
    default=None,
    help="A comma separated list indicating what service or custom tags should be used to filter the list of monitors",
)

args = vars(parser.parse_args())
purpose = args.pop("purpose")
datadog_query = args

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
full_monitors = datadog.api.Monitor.get_all(**datadog_query)
monitors = [output_monitor(m, purpose) for m in full_monitors]
print(yaml.dump(monitors))
