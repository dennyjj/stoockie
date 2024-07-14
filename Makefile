.PHONY: install deploy


BASE_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))


install:
	@cd $(BASE_DIR)/package && pip install -r requirements.txt

deploy:
	@cd $(BASE_DIR)/cdk && cdk deploy --require-approval never
