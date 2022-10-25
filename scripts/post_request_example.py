import requests

def shorten_url(url: str = '') -> str:
    """Shorten a URL using the gotiny API."""

    if not url:
        raise ValueError('URL cannot be empty')

    base_url = 'https://gotiny.cc/api'
    headers = {'Accept': 'application/json'}
    params = {'input': url}

    request = requests.post(base_url, headers=headers, json=params)
    print(request.status_code)

    return request.json()



def main() -> None:
    url = 'https://www.google.com'
    shortened_url = shorten_url(url)
    print(shortened_url)

    base_url = 'https://gotiny.cc'
    print(f'{base_url}/{shortened_url[0]["code"]}')



if __name__ == '__main__':
    main()