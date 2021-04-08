#!/bin/bash
# This script displays all the HTTP methods the server
# of a given URL will accept.
curl --head -s "$1" | grep Allow: | cut -d' ' -f2-
