import requests


KING_URL = 'https://wttr.in/'


if __name__ == '__main__':
    url1 = f'{KING_URL}london&?m&?M&lang=ru'
    response1 = requests.get(url1)
    response1.raise_for_status()
    print(response1.text)

    url2 = f'{KING_URL}svo&?m&?M&lang=ru'
    response2 = requests.get(url2)
    response2.raise_for_status()
    print(response2.text)

    url3 = f'{KING_URL}Череповец&?m&?M&lang=ru'
    response3 = requests.get(url3)
    response3.raise_for_status()
    print(response3.text)