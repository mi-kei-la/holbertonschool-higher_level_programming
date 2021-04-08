#!/bin/bash
# This script gets the body size of a given URL.
curl --head "$1" -s | grep Content-Length | cut -d' ' -f2
