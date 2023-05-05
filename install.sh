#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "installing to default location"
    source util/cp-no-bin; run-from-project-root
elif [[ $# -eq 1 ]]; then
    echo "argument detected"
    if [[ -d $1 ]]; then
        echo "installing to $1"
        source util/cp-no-bin; run-from-project-root $1
    else
        mkdir -p $1
        source util/cp-no-bin; run-from-project-root $1
    fi
fi