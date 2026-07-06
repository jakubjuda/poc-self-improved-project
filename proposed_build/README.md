# POC Self-Improved Project: Vendor-Neutral LLM ETL

A production-ready ETL pipeline using Polars, DuckDB, and LiteLLM for vendor-neutral LLM processing.

## Requirements
- [uv](https://github.com/astral-sh/uv) installed.
- Docker (optional, for containerized runs).

## Quickstart
1. Copy `.env.example` to `.env` and add your API keys (e.g., `OPENAI_API_KEY`).
2. Run `make setup` to install dependencies and run the pipeline.

## Commands
- `make setup`: Install dependencies and run.
- `make run`: Run the pipeline.
- `make build`: Build the OCI-compliant Docker image.
- `make clean`: Remove virtual environments and local database.
