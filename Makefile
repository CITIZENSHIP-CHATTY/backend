IMAGE ?= chatty:develop
TEST_IMAGE ?= chatty:develop-test

.EXPORT_ALL_VARIABLES:

run-d: COMPOSE ?= docker-compose -f compose-base.yml -f compose-local.yml
run-d: build
	$(COMPOSE) -f compose-local.yml up -d

run: COMPOSE ?= docker-compose -f compose-base.yml -f compose-local.yml
run: build
	$(COMPOSE) up

run-dev: COMPOSE ?= docker-compose -f compose-base.yml -f compose-dev.yml
run-dev: build
	$(COMPOSE) -f compose-dev.yml up -d
rm:
	$(COMPOSE) stop
	$(COMPOSE) rm -f

build:
	docker build -t $(IMAGE) .
	docker build -t $(TEST_IMAGE) .

test: COMPOSE_TEST ?= docker-compose -f compose-base.yml -f compose-integration.yml
test: build
	docker rm -f chatty-test || true
	$(COMPOSE_TEST) up -d web
	$(COMPOSE_TEST) run --name chatty-test web \
		pytest -v -q

logs:
	$(COMPOSE) logs -f web
