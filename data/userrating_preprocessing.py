import os
import json
import requests
import time

data = []
jikan_base_url_user = "https://api.jikan.moe/v3/user/"

def get_user_id(username):
    url = jikan_base_url_user + username
    try:
        response = requests.get(url).json()
        return response["user_id"]
    except Exception:
        time.sleep(1)
        return get_user_id(username)

no_rating = 0

file_list = os.listdir(r'./ratings')
for file in file_list:
    if file.startswith('user_ratings_anime_'):
        anime_id = file.split('_')[-1].split('.')[0]
        with open(r'./ratings/{}'.format(file), 'r') as f:
            user_ratings = json.load(f)
            f.close()
        for user_rating in user_ratings:
            username = user_rating["username"]
            score = user_rating["score"]
            if score is None:
                score = -1
                no_rating += 1
            data.append({
                "username": username,
                "anime_id": anime_id,
                "rating": score
            })
        print("Finished getting user ratings for anime {}".format(anime_id))


print("Number of edges: ", len(data) - no_rating)
with open('all_user_ratings.json', 'w+') as f:
    json.dump(data, f)
    f.close()