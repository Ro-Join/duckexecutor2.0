#!/bin/bash

# Define the URL and cookies names
URL="https://www.roblox.com/home"
COOKIE1_NAME=".ROBLOSECURITY"
COOKIE2_NAME=".RBXIDCHECK"

# Retrieve the cookies using curl
COOKIE1=$(curl -s --cookie-jar - "$URL" | grep "$COOKIE1_NAME" | awk '{print $7}')
COOKIE2=$(curl -s --cookie-jar - "$URL" | grep "$COOKIE2_NAME" | awk '{print $7}')

# Call the Python script with the cookies as arguments
python3 script.py "$COOKIE1" "$COOKIE2"
