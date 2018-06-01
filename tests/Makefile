.PHONY: help deploy_container_env clean_docker

.DEFAULT: help
# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

CURDIRR = $(abspath $(CURDIR))

TARGET_MAX_CHAR_NUM=25
## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

VENV_NAME = venv
VENV_PATH=$(CURDIR)/$(VENV_NAME)
VENV_BIN=$(VENV_PATH)/bin
PYTHONPATH = PYTHONPATH=PYTHONPATH:$(VENV_PATH)/lib/python2.7/site-packages:$(VENV_PATH)/lib/python3.6/site-packages
VENV_ACTIVATE =. $(VENV_BIN)/activate
PYTHON = $(PYTHONPATH) $(VENV_BIN)/python

INVENTORY = containers/1router_1brouker_1client/inventory.yaml
ANSIBLE_ARGS = -i $(INVENTORY) -vvv
ANSIBLE_PLAYBOOK = $(VENV_ACTIVATE) && $(PYTHONPATH) $(VENV_BIN)/ansible-playbook $(ANSIBLE_ARGS) 

containers = client1 broker1 router1
clean_docker = docker rm -f $(containers) || true

all: deploy_container_env

## Create virtual environment
venv: $(VENV_BIN)/activate
	@echo "Activating virtual environment..."
$(VENV_BIN)/activate: requirements.txt
	test -d $(VENV_PATH) || virtualenv $(VENV_PATH)
	$(VENV_BIN)/pip install -Ur requirements.txt
	touch $(VENV_BIN)/activate

## Deploy docker containers
deploy_container_env: clean_docker venv
	@echo "Deploying docker containers..."
	$(ANSIBLE_PLAYBOOK) containers/1router_1brouker_1client/main.yaml

## Clean docker containers
clean_docker:
	@echo "Cleaning docker containers..."
	$(clean_docker)
