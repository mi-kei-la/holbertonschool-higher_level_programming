#!/bin/bash
# This script sends a POST request to a given URL.
curl -d "email=hr@holbertonschool.com" -d subject="I will always be here for PLD" "$1"
