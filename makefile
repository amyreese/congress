
server:
	python app.wsgi

shell:
	python -i app.wsgi

.PHONY:
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

