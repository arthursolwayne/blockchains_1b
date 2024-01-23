import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    json_data = json.dumps(data)
    url = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
    headers = {
        'pinata_api_key': '794ed328fa15c4b6c180',
        'pinata_secret_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIxYjA0OGZmMi0xMWNkLTRhODMtOWQ4NC1lYWZkMGU4YWEzNzIiLCJlbWFpbCI6ImFydHdheW5lQHNlYXMudXBlbm4uZWR1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6Ijc5NGVkMzI4ZmExNWM0YjZjMTgwIiwic2NvcGVkS2V5U2VjcmV0IjoiYmIxNDhiNmZmMTUyODZkMWMwNmFlMGE4ZGFmNTAzYWE0M2Y4YjhlNTdjMmFlMzM5OWU3MjFjYzA5MzU3MGU1MSIsImlhdCI6MTcwNTk3ODM2Nn0.OZV19zQF7HSC0TaSoellqE7AyfIwfH4Onist5nORkbI'
    }
    response = requests.post(url, headers=headers, json={"pinataContent": data})
    cid = response.json()['IpfsHash']

    return cid


def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    url = f'https://gateway.pinata.cloud/ipfs/{cid}'
    response = requests.get(url)
    if content_type == "json":
        data = response.json()
    else:
        data = response.content
    assert isinstance(data, dict), "get_from_ipfs should return a dict when content_type is 'json'"
    return data
