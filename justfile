# Install all dependencies
install:
    uv sync --all-extras

# Run tests
test:
    uv run --extra test pytest

# Run tests with coverage
test-cov:
    uv run --extra test pytest --cov=./ --cov-report=xml

# Run type checking
typing:
    uv run --extra typing --extra test ty check hooks/ tests/

# Run linting and formatting
lint:
    uvx prek run -a -c .pre-commit-config.yaml

# Run all checks (format, lint, typing, test)
check: lint typing test

# Build docs and run doctests
docs:
    uv run --extra docs --extra test sphinx-build -n -T -b html -d docs/build/doctrees docs/source docs/build/html
    uv run --extra docs --extra test sphinx-build -n -T -b doctest -d docs/build/doctrees docs/source docs/build/html
