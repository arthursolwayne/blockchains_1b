import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    json_data = json.dumps(data)
    url = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
    headers = {
        'pinata_api_key': '1f7417685928a7ebda5b',
        'pinata_secret_api_key': '8abe3a2fa2b0b0ea74e9b7d414dbaf8674a5381a60477b897b08cd72baf1fe43'
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
