clean:
	coverage erase
	rm -rf .tox
	find . -name '*.pyc' -delete

quality:
	tox -e quality

requirements:
	pip install -r test_requirements.txt

test:
	tox

.PHONY: clean, quality, requirements
