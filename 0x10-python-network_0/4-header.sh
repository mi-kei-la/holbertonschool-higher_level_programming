#!/bin/bash
# This script sends a given header variable along
# with the GET request. and displays the body of
# a given URL.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
