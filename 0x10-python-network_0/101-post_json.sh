#!/bin/bash
# This script sends a JSON POST request to a given URL.
curl -s -d @"$2" -H "Content-Type: application/json" -X POST "$1"
