#!/bin/bash
# sends a POST request to the passed URL
curl -sX POST "$1" -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD'
