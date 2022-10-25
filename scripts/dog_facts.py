import requests

def dog_api(num_of_facts: int = 1, all: bool = False) -> any:
    """Get dog facts from the dog API."""

    if not all:
        # If the user does not want to get all the facts, then get N number of facts
        url = f'https://dog-api.kinduff.com/api/facts?number={num_of_facts}'
    else:
        # If the user wants to get all the facts, then get all the facts
        url = 'https://dog-api.kinduff.com/api/facts?number=all'

    request = requests.get(url)
    print(request.status_code)
    # print(request.text) // Check the raw response
    facts = request.json()

    return facts['facts']


def main() -> None:
    """Main function."""

    saved_facts = dog_api(num_of_facts=3)

    for i, fact in enumerate(saved_facts):
        print(f"{i + 1}. {fact}\n")

    # Lets save my stored facts to a file
    with open('../data/dog_facts.txt', 'w') as file:
        for fact in saved_facts:
            file.write(f'{fact}')
            file.write('\n')


if __name__ == '__main__':
    main()