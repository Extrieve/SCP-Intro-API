import requests

# Lets make this more fun by getting dog videos
def dog_api():
    """Get dog videos from the dog API."""

    url = 'https://random.dog/woof.json'

    request = requests.get(url)
    print(request.status_code)
    # print(request.text) // Check the raw response
    video_url = request.json()['url']
    return video_url


def main() -> None:
    dog_video_url = dog_api()
    print(dog_video_url)

    # Lets store the video url in a file
    video_request = requests.get(dog_video_url)
    with open('../data/dog_video.mp4', 'wb') as file:
        file.write(video_request.content)


if __name__ == '__main__':
    main()