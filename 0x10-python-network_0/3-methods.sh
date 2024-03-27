#!/bin/bash
# Script that displays all HTTP methods the server will accept
curl -sX OPTIONS "$1"
