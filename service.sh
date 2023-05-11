#!/bin/bash

me=$(basename $0)
dockerfile="dockerfile-pg"
image_name="pg-gitea" && image_tag="v0.1.0"
patched_pg_image="${image_name}:${image_tag}"


echo "usage: $(basename $0) < up | down | install >"

build_image_if_not_detected () {
    echo "[${me}] looking for patched image..."
    # see: https://stackoverflow.com/questions/30543409/how-to-check-if-a-docker-image-with-a-specific-tag-exist-locally
    if [[ "$(docker images -q ${patched_pg_image} 2> /dev/null)" == "" ]]; then
        echo "patched image not detected"
        echo "building image..."
        # do something
        # in this case, build the image
        
        docker build --file ${dockerfile} --tag ${patched_pg_image} .
        
        if [[ $? -eq 0 ]];then
            echo "Patched image successfully created"
        fi
    else
        echo "[OK] patched image detected"
    fi

}

build_image_if_not_detected


if [[ $1 == "up" ]]; then
    python util/docker-compose.py up
fi

if [[ $1 == "down" ]]; then
    python util/docker-compose.py down
fi

