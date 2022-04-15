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
