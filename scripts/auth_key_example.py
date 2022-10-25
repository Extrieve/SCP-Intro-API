'''
For the following example you will need to have a valid API key and secret
Go to https://www.remove.bg/api#remove-background create an account and get your API key
'''

import requests
from secrets import my_secret

def remove_background_from_img_file(input_file_path, filename, api_key = '') -> None:

    if not api_key:
        raise Exception('You need to set your API key')

    output_file_path = '../data/' + filename + '_no_bg.png'

    with open(input_file_path, 'rb') as f:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': f},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )
        if response.status_code == requests.codes.ok:
            with open(output_file_path, 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)



def main() -> None:
    api_key = my_secret
    filename = 'cat'
    input_file_path = '../file-inputs/cat.jpg'
    remove_background_from_img_file(input_file_path, filename, api_key)



if __name__ == '__main__':
    main()