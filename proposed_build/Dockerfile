# syntax=docker/dockerfile:1
FROM python:3.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
# Copy dependency definitions
COPY pyproject.toml uv.lock* ./

# Install dependencies into a virtual environment
RUN uv sync --frozen --no-dev --no-install-project || uv sync --no-dev --no-install-project

# Copy source code and install the project
COPY src/ ./src/
RUN uv sync --frozen --no-dev || uv sync --no-dev

FROM python:3.11-slim AS runtime

# OCI-compliant labels
LABEL org.opencontainers.image.title="poc-self-improved-project"
LABEL org.opencontainers.image.description="Vendor-neutral LLM ETL/ELT pipeline"
LABEL org.opencontainers.image.source="https://github.com/yourorg/poc-self-improved-project"
LABEL org.opencontainers.image.vendor="YourOrg"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

# Copy virtual environment and source code from builder
COPY --from=builder /app/.venv /app/.venv
COPY src/ ./src/

# Ensure the virtual environment is used
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

ENTRYPOINT ["python", "-m", "src.main"]
