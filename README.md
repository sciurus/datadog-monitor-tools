# Introduction

There are lots of tools (e.g. Terraform, DogPush, BarkDog) that you can use to manage your DataDog monitors as code. You should probably use one of them. But what if you aren't, yet you still need to refactor a bunch of monitors? The scripts in this repo will let you export some or all of your monitors to a YAML file, edit them, then sync your edits back to DataDog.

In the future I may add a script to create new monitors as well.

# Installation

This requires a working Python 3 environment.

1. Clone this repo
1. `pip install datadog pyyaml`

# Usage

1. `./get_monitors.py > foo.yml`
1. Make your changes to foo.yml
1. `./update_monitors.py foo.yml`

get_monitors.py allows you to filter the monitors to download by name, tag, and monitor tag as described at https://docs.datadoghq.com/api/?lang=python#get-all-monitor-details
