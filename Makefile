clean:
	coverage erase
	rm -rf .tox
	find . -name '*.pyc' -delete

quality:
	tox -e quality

requirements:
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip_tools.txt
	pip-sync requirements/test.txt

test:
	tox

.PHONY: clean, quality, requirements, check_keywords

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -q -r requirements/pip_tools.txt
	pip-compile --rebuild --upgrade --allow-unsafe -o requirements/pip.txt requirements/pip.in
	pip-compile --upgrade -o requirements/pip_tools.txt requirements/pip_tools.in
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
	pip-compile --upgrade -o requirements/doc.txt requirements/doc.in
	pip-compile --upgrade -o requirements/test.txt requirements/test.in
	pip-compile --upgrade -o requirements/tox.txt requirements/tox.in
	pip-compile --upgrade -o requirements/ci.txt requirements/ci.in
	# Let tox control the Django version version for tests
	grep -e "^django==" requirements/test.txt > requirements/django.txt
	sed '/^[dD]jango==/d' requirements/test.txt > requirements/test.tmp
	mv requirements/test.tmp requirements/test.txt

check_keywords: ## Scan the Django models in all installed apps in this project for restricted field names
	python manage.py check_reserved_keywords --override_file db_keyword_overrides.yml
