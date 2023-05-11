#!/bin/bash

echo "usage: $(basename $0) <up|down>"

if [[ $1 == "up" ]]; then
    python util/docker-compose.py up
fi

if [[ $1 == "down" ]]; then
    python util/docker-compose.py down
fi