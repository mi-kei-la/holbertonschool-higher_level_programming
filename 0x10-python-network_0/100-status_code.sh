#!/bin/bash
# This script displays the status code of an URL request.
curl -s -o /dev/null -w "%{http_code}" "$1"
