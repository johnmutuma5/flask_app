venv:
	virtualenv -p python3.7 venv

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run:
	python run.py

tables:
	python seeds.py

test:
	nosetests --exe  --nocapture --with-coverage --cover-package=app
