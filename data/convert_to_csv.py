import json
from scraper.scraper import get_anime_data_from_list
import csv

def convert_ratings_to_csv(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        f.close()
    with open('rating.csv', 'w+') as ff:
        ff.write('username,anime_id,rating\n')
        for user_rating in data:
            username = user_rating["username"]
            anime_id = user_rating["anime_id"]
            rating = user_rating["rating"]
            ff.write('{},{},{}\n'.format(username, anime_id, rating))
        ff.close()
    print("Finished converting {}".format(file_path))

def convert_anime_list_to_csv(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        f.close()
    anime_list = data["top_animes"][:200]
    anime_data = get_anime_data_from_list(anime_list)
    keys = anime_data[0].keys()
    for anime in anime_data:
        # force utf-8 encoding
        anime["name"] = anime["name"].encode('utf-8')
    with open('anime.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()   
        dict_writer.writerows(anime_data)

if __name__=="__main__":
    convert_ratings_to_csv('./all_user_ratings.json')
    #convert_anime_list_to_csv('./top_1000_animes.json')