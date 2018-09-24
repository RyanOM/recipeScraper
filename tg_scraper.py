import requests
import random

# Example of recipe api url: https://www.tudogostoso.com.br/api/recipes/5351/
BASE_URL = "https://www.tudogostoso.com.br/api/recipes/"

def random_recipe():
    i = random.randint(100, 50000)
    url = BASE_URL + str(i)
    r = requests.get(url)
    return(r.text)


def main():
    print(random_recipe())


if __name__ == '__main__':
    main()