.PHONY: install deploy

install:
	@pip install -r requirements.txt

deploy:
	@cdk deploy --require-approval never
