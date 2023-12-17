import requests

url = 'http://localhost:5000'
data = {
    'data': {
        "elements": [8, 7, 6, 5, 4],
        "subset_number": 2}
        }

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()['result']
    print(f'Result: {result}')
else:
    print(f'Error: {response.status_code}, {response.json()}')