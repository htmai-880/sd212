import json

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

if __name__=="__main__":
    convert_ratings_to_csv('./all_user_ratings.json')