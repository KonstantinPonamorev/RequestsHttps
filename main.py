import requests
from pprint import pprint

def get_heroes_ids():
    heroes = list(input('Введите героев через запятую :').split(', '))
    heroes_ids = {}
    for hero in heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        response = requests.get(url)
        for result in response.json()['results']:
            if result['name'] == hero:
                heroes_ids[f'{hero}'] = result['id']
            else:
                ...
    return heroes_ids

def compare_heroes_by_intelligence():
    heroes_ids = get_heroes_ids()
    max_int = 0
    smartest_hero = ''
    for hero in heroes_ids:
        url = f'https://superheroapi.com/api/2619421814940190/{heroes_ids.get(hero)}/powerstats'
        powerstats = requests.get(url)
        intelligence = int(powerstats.json().get('intelligence'))
        if intelligence > max_int:
            max_int = intelligence
            smartest_hero = hero
        else:
            ...
    pprint(f'Самый умный супергерой: {hero} (интеллект = {max_int})')



if __name__ == '__main__':
    compare_heroes_by_intelligence()


