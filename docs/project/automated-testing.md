# Automated Testing Documentation

To be able to automate the full test suite of the project to ensure
general compliance, you will need to run the following Docker Compose file.
This file should be ran from the root project directory everytime.

```sh
docker compose -f test-docker-compose.yml up
```

This Docker Compose file is what is used during CI in Github actions to
ensure version bumping and PyPi release can take place.