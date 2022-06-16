import requests
import json
import sys

jikan_base_url = "https://api.jikan.moe/v3/anime/"

def get_user_ratings(anime_id):
    anime_url = jikan_base_url + str(anime_id) + '/userupdates/'
    data = []
    for i in range(1,6):
        print("page ", i)
        response = requests.get(anime_url + str(i)).json()
        data.extend(response["users"])
    print("Finished getting user ratings for anime {}".format(anime_id))
    return data

def get_user_ratings_top_anime(k):
    with open('top_1000_animes.json', 'r') as f:
        data = json.load(f)
        f.close()
    anime_list = data["top_animes"]
    for i in range(k, len(anime_list)):
        anime = anime_list[i]
        anime_id = anime["node"]["id"]
        data = get_user_ratings(anime_id)
        with open('ratings/user_ratings_anime_{}.json'.format(anime_id), 'w+') as ff:
            json.dump(data, ff)
            ff.close()

import os

# folder path
dir_path = r'./ratings'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

get_user_ratings_top_anime(count)
        
