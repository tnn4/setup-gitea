# Setup gitea service

set up database: https://docs.gitea.io/en-us/installation/database-prep/#postgresql-1

with docker

Run bash inside docker container
- `docker exec --interactive --tty <your-postgres-container> bash`

Open database server, login as super user
- `$ su -c "psql" - postgres`

Create database user(role) with login privilege and password, replace the password if remote
```sql
psql# CREATE ROLE gitea WITH LOGIN PASSWORD 'gitea';
```
Create database with UTF-8 charaset and owned by `gitea`
```sql
CREATE DATABASE giteadb WITH OWNER gitea TEMPLATE template0 ENCODING UTF8 LC_COLLATE 'en_us.UTD-8' LC_CTYPE 'en_US.UTF-8';
```

Allow user to access database with the following authentication rules in `pg_hba.conf`
- local: `local giteadb gitea scram-sha-256`
- remote: `host giteadb gitea 192.0.2.10/32 scram-sha-256`
- for remote, replace db-name, user and IP with yours

restart postgres to apply the rules

test connection to database
- `psql -U gitea -d diteadb`

remote
- psql "postgres://gitea@<your-ip>/giteadb" where <your-ip> is something like `203.0.113.3`
    - you should be prompted for a password