import requests

if __name__ == '__main__':
    payload = {
        "m": "",
        "M": "",
        "T": "",
        "n": "",
        "lang": "ru"
    }
    cities = [
        "london",
        "svo",
        "Череповец"
    ]
    for city in cities:
        response = requests.get(f'https://wttr.in/{city}', params=payload)
        response.raise_for_status()
        print(response.text)
