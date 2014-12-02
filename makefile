
server:
	python app.wsgi

shell:
	@which ipython && ipython -i app.wsgi || python -i app.wsgi

lint:
	flake8 --show-source .

test: lint
	python app.wsgi --no-run

.PHONY:
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

