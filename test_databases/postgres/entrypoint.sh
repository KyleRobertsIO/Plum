#!/bin/bash
pg_ctl start

PGPASSWORD=$POSTGRES_DB_PASSWORD

psql -h "127.0.0.1" \
-U $POSTGRES_DB_USERNAME \
-d $POSTGRES_DB_NAME \
-a -f "/workspace/setup.sql"

while $true
do
    sleep 1
done