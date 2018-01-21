import uuid

import pytest

from github_fetcher import fetch_github_profile


def test_fetcher_returns_data():
    profile = fetch_github_profile('paultiplady')
    assert profile['login'] == 'paultiplady'


def test_fetcher_raises_error_for_nonexistant():
    with pytest.raises(Exception):
        # UUIDs are statistically unique, so this profile name can't be taken.
        random_profile_name = uuid.uuid4()
        fetch_github_profile(random_profile_name)
