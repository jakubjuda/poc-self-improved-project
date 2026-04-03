.PHONY: setup install run build clean lint test

setup: install run

install:
	uv sync

run:
	uv run python -m src.main

build:
	docker build -t poc-llm-etl .

clean:
	rm -rf .venv
	rm -f local_data.duckdb
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	uv run ruff check .
	uv run ruff format .

test:
	uv run pytest
