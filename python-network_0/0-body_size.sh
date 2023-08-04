#!/bin/bash
# sends a request
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
