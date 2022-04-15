# Simple Flask Docker

A simple python Flask app that will be package as docker image

## Usage

### Configuration

| ENV_VAR_NAME |        Description        |  default  | required |
| :----------: | :-----------------------: | :-------: | :------: |
|  FLASK_HOST  |    host to bind flask     | localhost |    no    |
|  FLASK_PORT  |    port to bind flask     |   8080    |    no    |
| FLASK_DEBUG  | start flask in debug more |   false   |    no    |

## Development

### Requirements

- python >= 3.7
- poetry

```
poetry install
```

### Docker

#### Linter
To enforce Dockerfile syntax we are using [hadolint](https://github.com/hadolint/hadolint)

```
hadolint Dockerfile
```

#### Test
We are testing the Docker image with [pytest-testinfra](https://github.com/pytest-dev/pytest-testinfra).

_Note: as this is a runtime test you need to be able to run the docker image to test it_

```
# poetry install
pytest --verbose tests/docker
```
