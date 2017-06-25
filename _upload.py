#!/usr/bin/env python
# coding: utf-8
"""Hochladen in die GAE"""

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))
PROJECTNAME = "statisch-test-01"
PROJECTVERSION = "1"

print PROJECTNAME

args = [
    os.path.expanduser("~/bin/google-cloud-sdk/bin/gcloud"),
    "app",
    "deploy",
    "--project", PROJECTNAME,
    "--version", PROJECTVERSION,
    "--quiet",
    # "--verbosity", "info",
    "app.yaml"
]

returncode = subprocess.call(args = args, cwd = THISDIR)
if returncode != 0:
    raw_input("Press ENTER to continue...")
