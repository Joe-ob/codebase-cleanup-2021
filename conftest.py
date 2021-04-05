
#
# this is the conftest.py file
#
# the presence of this file, even if empty
# ... helps the pytest package collect and run all tests in the test dir
#

import pytest
from app.robo import fetch_data

@pytest.fixture(scope="module")
def parsed_googl_response():
    return fetch_data("GOOGL")

@pytest.fixture(scope="module")
def parsed_oops_response():
    return fetch_data("OOPS")