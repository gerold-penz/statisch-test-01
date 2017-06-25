#!/usr/bin/env python
# coding: utf-8
"""Startet dev_appserver.py"""

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))

subprocess.call(
    args = [
        os.path.expanduser(
            "~/bin/google-cloud-sdk/platform/google_appengine/dev_appserver.py"
        ),
        "--host", "0.0.0.0",
        "./app.yaml"
    ],
    cwd = THISDIR
)
