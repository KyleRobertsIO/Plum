# Plum Project

An in house ETL framework for moving data to where it has to go.

## Development

Running the postgres database independantly...

```sh
docker rmi postgres-postgres -f && \
docker system prune -f && \
docker compose -f ./test_databases/postgres/docker-compose.yml up
```