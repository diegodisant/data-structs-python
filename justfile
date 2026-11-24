# data-structs-python — development tasks
# Install: https://github.com/casey/just

# Python interpreter: prefer the project virtualenv when present
python := if path_exists('.venv/bin/python3') == 'true' { '.venv/bin/python3' } else { 'python3' }

# Make the structs package importable (equivalent of the old set-path.sh)
export PYTHONPATH := justfile_directory()

# List available recipes (default)
default:
    @just --list

# Run the whole test suite
test:
    {{python}} -m pytest tests/

# Run a single test by name, e.g. `just test-single test_search_in_1m_items`
test-single test_name:
    {{python}} -m pytest -s -vv tests/ -k '{{test_name}}'

# Run tests with coverage report
test-coverage:
    {{python}} -m pytest --cov=structs --cov-report=html tests/

# Run a test under the memory profiler, e.g. `just test-memory list/test_single_list test_search_in_1m_items`
test-memory test_path test_name:
    {{python}} -m memory_profiler pytest -s -vv tests/{{test_path}}.py -k '{{test_name}}'

# Run pylint over sources and tests
lint:
    {{python}} -m pylint --recursive=y structs tests

# Open a cProfile .prof file in snakeviz, e.g. `just profile-open test_binary_tree`
open-profile test_name:
    {{python}} -m snakeviz profiling/{{test_name}}.prof

# Install pinned dependencies into the active environment
setup:
    {{python}} -m pip install -r requirements.txt
