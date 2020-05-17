![Chatty](https://github.com/CITIZENSHIP-CHATTY/backend/workflows/Chatty/badge.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## CHATTY
Back-end part of chatty chat application

# DEVELOPMENT STUFF

## SYSTEM REQUIREMENTS

* Make
* Docker
* docker-compose

# USAGE

#### Running api service

```bash
make run
```

#### Running api service as daemon

```bash
make run-d
```

#### Build an docker image

```bash
make build
```

#### Running with gunicorn and nginx (for deploying)

```bash
make run-dev
```

#### Removing service containers

```bash
make rm
```

#### Running tests

```bash
make test
```
