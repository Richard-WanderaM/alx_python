#!/usr/bin/env python3
"""
Module to fetch and display the status of a website.
"""

import requests

def fetch_custom_status():
    """
    Fetches and displays the status of http://0.0.0.0:5050/status.
    """
    url = 'http://0.0.0.0:5050/status'
    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text

    print("Body response:")
    print(f"\t- type: <{content_type}>")
    print(f"\t- content: {content}")

if __name__ == "__main__":
    fetch_custom_status()

