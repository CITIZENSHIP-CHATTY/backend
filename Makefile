COMPOSE ?= docker-compose -f compose-local.yml
IMAGE ?= chatty:develop
TEST_IMAGE ?= chatty:develop-test

.EXPORT_ALL_VARIABLES:

run-d: build
run-d:
	$(COMPOSE) up -d

run: build
run:
	$(COMPOSE) up

rm:
	$(COMPOSE) stop
	$(COMPOSE) rm -f

build:
	docker build -t $(IMAGE) .
	docker build -t $(TEST_IMAGE) .

test: COMPOSE_TEST ?= docker-compose -f compose-integration.yml
test: build
	docker rm -f chatty-test || true
	$(COMPOSE_TEST) up -d web
	$(COMPOSE_TEST) run --name chatty-test web \
		pytest -v -q

logs:
	$(COMPOSE) logs -f web
