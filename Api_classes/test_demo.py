import warnings
import urllib3

# Suppress that persistent SSL warning in your test runs
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

import pytest
import requests


def test_getrequest_validation():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    base_url = 'https://reqres.in'

    # Try adding allow_redirects=True to ensure you aren't hitting an auth-wall redirect
    response = requests.get(url=base_url + '/api/users/2', headers=header, allow_redirects=True)

    assert response.status_code == 200