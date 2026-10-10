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
	pycodestyle --config=.pycodestyle src/django_sites_extensions
	pylint --rcfile pylintrc src/django_sites_extensions
	python -m build --wheel
	twine check dist/*

.PHONY: requirements
requirements: ## Install test requirements
	uv sync --locked --group dev

.PHONY: test
test: ## Run tests
	pytest --cov --cov-report=xml

.PHONY: upgrade
upgrade: ## update python dependencies
	uv run --with edx-lint edx_lint write_uv_constraints pyproject.toml
	uv lock --upgrade
