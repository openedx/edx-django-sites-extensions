.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: clean
clean: ## Remove generated files and tox environments
	coverage erase
	rm -rf .tox
	find . -name '*.pyc' -delete

.PHONY: quality
quality: ## Run quality checks (pycodestyle, pylint)
	tox -e quality

.PHONY: requirements
requirements: ## Install test requirements
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip_tools.txt
	pip-sync requirements/test.txt

.PHONY: test
test: ## Run tests using tox
	tox

.PHONY: upgrade
upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## Update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -q -r requirements/pip_tools.txt
	pip-compile --rebuild --upgrade --allow-unsafe -o requirements/pip.txt requirements/pip.in
	pip-compile --upgrade -o requirements/pip_tools.txt requirements/pip_tools.in
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip_tools.txt
	pip-compile --upgrade --allow-unsafe -o requirements/base.txt requirements/base.in
	pip-compile --upgrade --allow-unsafe -o requirements/doc.txt requirements/doc.in
	pip-compile --upgrade --allow-unsafe -o requirements/test.txt requirements/test.in
	pip-compile --upgrade --allow-unsafe -o requirements/tox.txt requirements/tox.in
	pip-compile --upgrade --allow-unsafe -o requirements/ci.txt requirements/ci.in
	# Let tox control the Django version version for tests
	grep -e "^django==" requirements/test.txt > requirements/django.txt
	grep -e "^asgiref==" requirements/test.txt >> requirements/django.txt
	sed '/^[dD]jango==/d' requirements/test.txt > requirements/test.tmp
	mv requirements/test.tmp requirements/test.txt
	sed '/^asgiref==/d' requirements/test.txt > requirements/test.tmp
	mv requirements/test.tmp requirements/test.txt
