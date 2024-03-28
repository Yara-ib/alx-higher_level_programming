#!/bin/bash
# script that sends a JSON POST request
curl -sd "@$2" "$1" -H "Content-Type: application/json"
