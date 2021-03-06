#!/usr/bin/python3
"""
module json api 8
"""


from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        l = ""
    else:
        l = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": l}
    r = requests.post(url, data=values)

    try:
        req = r.json()
        if req:
            print("[{}] {}".format(req.get("id"), req.get("name")))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
