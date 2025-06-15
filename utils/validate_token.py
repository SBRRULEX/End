# utils/validate_token.py

import requests

def is_token_valid(token):
    """
    Checks if the provided Facebook token is valid.
    Returns True if valid, False otherwise.
    """
    try:
        url = f"https://graph.facebook.com/me?access_token={token}"
        response = requests.get(url)
        data = response.json()

        return "id" in data
    except Exception as e:
        print(f"Token validation error: {e}")
        return False
