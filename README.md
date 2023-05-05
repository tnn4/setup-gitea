# Gitea configuration

## Set up gitea service
look [here](./setup-gitea-service.md)

# Use with docker compose
`$ docker compose -f <your-docker-compose.yml> up`

## Volume mappings

| host | container |
| --- | --- |
|`pg-gitea-data`| `/var/lib/postgres/data/`|
