
.PHONY: pylint

# Run pylint on all Python files in the src/ directory
pylint:
	@echo "Running pylint on source code..."
	@pylint .

# Run black on all Python files in the src/ directory
format:
	black src .

