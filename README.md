# Gitea setup guide

platform: Ubuntu 22.04

## Directory structure
- `bin` - put your binaries here
- `custom` - files for customizing gitea, https://docs.gitea.io/en-us/administration/customizing-gitea/
- `docker` - volumes for docker, https://docs.gitea.io/en-us/installation/install-with-docker/
- `util` - convenience scripts
- `.git` - files used with git

## Download gitea
download: [here](https://docs.gitea.io/en-us/installation/install-from-binary/)

put the binary into the `bin` folder, the default `gitea.service` file uses that to run

## Set up gitea service from binary

If using without docker, 
look [here](./setup-gitea-service.md)

[original_src](https://docs.gitea.io/en-us/installation/install-from-binary/) for more details

---

## Use with docker compose
[see](https://docs.gitea.io/en-us/installation/install-with-docker/)

### Start services

if compose file is the default: `docker-compose.yml`:
- `docker compose up`

if custom file name:
- `$ docker compose -f <your-docker-compose.yml> up`

this repo:
- `$ docker compose -f docker-gitea-compose-v3.yml up` 

### Volume mappings

| host | service | container |
| --- | --- | --- |
|`docker/gitea-data`| gitea | `/data` |
|`docker/gitea-pg-data`| db | `/var/lib/postgres/data/`|

---
