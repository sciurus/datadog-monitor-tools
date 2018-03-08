# Introduction

There are lots of tools (e.g. Terraform, DogPush, BarkDog) that you can use to manage your DataDog monitors as code. You should probably use one of them. But what if you aren't, yet you still need to refactor a bunch of monitors? The scripts in this repo will let you export some or all of your monitors to a YAML file, edit them, then sync your edits back to DataDog.

In the future I may add a script to create new monitors as well.

# Installation

This requires a working Python 3 environment.

1. Clone this repo
1. `pip install datadog pyyaml`

# Usage

## Prerequisites

1. Set up an API and application key at https://app.datadoghq.com/account/settings#api
1. `export DD_API_KEY=your_api_key`
1. `export DD_APP_KEY=your_app_key`

## Basic Usage

1. `./get_monitors.py > foo.yml`
1. Make your changes to foo.yml
1. `./update_monitors.py foo.yml`

## Advanced Usage

get_monitors.py allows you to filter the monitors to download by any combination of name, tag, and monitor tag as described at https://docs.datadoghq.com/api/?lang=python#get-all-monitor-details. For example, `get_monitors.py --tags 'env:foo,app:bar'`
