import requests

url = "https://apilayer.com/marketplace/exchangerates_data-api?access_key=2130b8f33395570b554d0e51114c86e4&base=EUR"

payload = {}
headers = {
    "apikey": "2130b8f33395570b554d0e51114c86e4"
}

response = requests.request("GET", url, headers=headers, data=payload)
result_json = response.json()

print(result_json)
