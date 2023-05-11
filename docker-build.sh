#!/bin/bash

dockerfile="dockerfile-pg"
image_name="tnn4/pg-gitea" && image_tag="v0.1.0"
patched_pg_image="${image_name}:${image_tag}"

docker build --file ${dockerfile} --tag ${patched_pg_image} .