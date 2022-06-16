from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
import requests
import csv

from scraper.scraper import top_animes, get_token, get_anime_data_from_list

app = Flask(__name__)
api = Api(app)

code = ''
state = ''

class Anime(Resource):
    def get(self):
        return {'I love': 'anime'}

class TopAnimes(Resource):
    def get(self):
        code = request.args.get('code')
        state = request.args.get('state')
        token = get_token(code)
        data = top_animes(token, count=1000)
        with open('top_1000_animes.json', 'w+') as f:
            json.dump({'top_animes': data}, f)
            f.close()
        return {'top_animes': data}, 200

class AnimeInfo(Resource):
    def get(self):
        with open('top_1000_animes.json', 'r') as f:
            data = json.load(f)
            f.close()
        anime_list = data["top_animes"]
        anime_data = get_anime_data_from_list(anime_list)
        keys = anime_data[0].keys()
        with open('anime.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(anime_data)
        return {'message': 'wrote data in anime.csv'}, 200

api.add_resource(Anime, '/')
api.add_resource(TopAnimes, '/top_animes')
api.add_resource(AnimeInfo, '/info')

if __name__ == '__main__':
    app.run(debug=True)