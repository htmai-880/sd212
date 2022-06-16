import requests

anime_base_url = "https://api.myanimelist.net/v2/anime/"
client_id = '97eabbc9ae2a1ecd2b151f2117b2e944'
code_verifier = 'skSTrGQGea-ZvwPyadTRxa7T507eryim7ojTkYQMEeKSIPCUD0AsTtVUTsQmq40sqrG_lh_wY1MyObw-TbFUPRJgW4w-nxhD4q4WMGAP5EOleMTdco7cYyBJKkBQGeWK'
jikan_base_url = "https://api.jikan.moe/v3/anime/"

# https://jikan.docs.apiary.io/#reference/0/search

def get_token(code):
    data = {
        'client_id': client_id,
        'code': code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post('https://myanimelist.net/v1/oauth2/token', data=data)
    print(response.json())
    return response.json()


def top_animes(token, count=100):
    ranking_url = anime_base_url + "ranking"

    my_token = token['access_token']

    amount=10
    offset=0

    headers = {
        'Authorization': 'Bearer ' + my_token,
    }
    params = {
        'ranking_type': 'all',
        'limit': amount,
        'offset': offset
    }
    
    top_list = []

    while len(top_list) < count:
        response = requests.get(ranking_url, headers=headers, params=params)
        data = response.json()
        print(data)
        top_list += data['data']
        offset += 10
        params['offset'] = offset

    return top_list

def get_anime_data(anime_id):
    anime_url = jikan_base_url + str(anime_id)
    response = requests.get(anime_url).json()

    genres = [g['name'] for g in response['genres']]

    data = {
        'anime_id': response['mal_id'],
        'name': response['title'],
        'genre': genres,
        'type': response['type'],
        'episodes': response['episodes'],
        'rating': response['score'],
        'members': response['members'],
    }
    return data

def get_anime_data_from_list(anime_list):
    data = []
    for anime in anime_list:
        print(anime['node']['title'])
        print(anime['ranking']['rank'])
        data.append(get_anime_data(anime['node']['id']))
    return data