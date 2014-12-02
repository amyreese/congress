
server:
	python app.wsgi

shell:
	@which ipython && ipython -i app.wsgi || python -i app.wsgi

.PHONY:
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

