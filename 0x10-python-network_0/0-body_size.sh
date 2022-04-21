#!/bin/bash
# Will display the size of the body of given URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
