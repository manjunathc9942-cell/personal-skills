import warnings
import urllib3

# Suppress that persistent SSL warning in your test runs
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

import pytest
import requests


def test_getrequest_validation():  # Fixed typo in function name too!
    header = {
        'Content-Type': 'application/json'  # FIXED: added the 'l' to application
    }
    base_url = 'https://reqres.in'

    response = requests.get(url=base_url + '/api/users/2', headers=header)

    assert 200 == response.status_code
    print(response.text)