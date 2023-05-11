#!/bin/bash

docker_pg="dockerfile-pg"

docker build --file $docker_pg --tag pg:gitea .