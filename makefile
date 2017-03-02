
server:
	python3 app.wsgi

shell:
	@which ipython3 && ipython3 -i app.wsgi || python3 -i app.wsgi

lint:
	flake8 --show-source .

test: lint
	python3 app.wsgi --no-run

.PHONY:
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

