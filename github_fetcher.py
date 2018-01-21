import requests


def fetch_github_profile(username):
    response = requests.get(url='https://api.github.com/users/%s' % username)
    if response.status_code == 404:
        raise Exception('User %s not found.' % username)

    return response.json()
