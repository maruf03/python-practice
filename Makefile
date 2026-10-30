.PHONY: format sort-import test

format:
	poetry run black .

sort-import:
	poetry isort .

test:
	poetry run pytest
