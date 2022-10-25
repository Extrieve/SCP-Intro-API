import requests

def get_anime_information(anime_name: str = '') -> any:
    """Get anime information from the Jikan API."""

    if not anime_name:
        raise ValueError('Anime name cannot be empty')

    url = 'https://api.jikan.moe/v4/anime'
    parameters = {'q': anime_name}

    request = requests.get(url, params=parameters)
    print(request.status_code)
    anime = request.json()

    return anime


def main() -> None:
    anime_search = get_anime_information('naruto')
    # print(anime_search.keys()) -> dict_keys(['pagination', 'data'])

    for anime in anime_search['data']:
        print(f"{anime['title']} ({anime['type']})")


if __name__ == '__main__':
    main()
