#!/usr/bin/python3
"""Uses the GitHub API to display user ID using Basic Authentication"""

import requests
import sys

def main():
    """Main function to fetch and display user ID using GitHub API"""
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    base_url = "https://api.github.com/user"

    response = requests.get(base_url, auth=(username, token))
    user_data = response.json()

    if "id" in user_data:
        print(user_data["id"])
    else:
        print("None")

if __name__ == "__main__":
    main()
