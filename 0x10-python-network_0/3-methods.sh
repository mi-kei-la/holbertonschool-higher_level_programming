#!/bin/bash
# This script displays all the HTTP methods of an URL.
curl -Is "$1" | grep Allow | cut -d' ' -f2-
