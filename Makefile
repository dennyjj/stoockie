.PHONY: deploy

deploy:
	@cd cdk && cdk deploy --require-approval never
