#!/bin/sh

# TODO: create a script to run all, single or with memory profiler a test

# run all tests
python3 -m pytest -s -vv tests/

# run a single test
python3 -m pytest -s -vv tests/ -k 'test_name'

# run with memory profiler
python3 -m memory_profiler pytest -s -vv tests/list/test_single_list.py -k 'test_search_in_1m_items'
