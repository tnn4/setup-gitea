#!/bin/bash

default_location="$HOME/service/gitea"

if [[ $# -eq 0 ]]; then
    echo "installing to default location: ${default_location}"
    source util/cp-no-bin; run-from-project-root
elif [[ $# -eq 1 ]]; then
    echo "argument detected"
    if [[ -d $1 ]]; then
        echo "installing to $1"
        source util/cp-no-bin; run-from-project-root $1
    else
        mkdir -p $1
        echo "created dir: $1"
        source util/cp-no-bin; run-from-project-root $1
    fi
fi