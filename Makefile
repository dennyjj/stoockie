.PHONY: install deploy

install:
	@pip install -r requirements.txt

deploy:
	@cd cdk && cdk deploy --require-approval never
