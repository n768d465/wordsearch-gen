from flask import Flask
from flask_restful import Resource, Api
from wordsearch_generator import WordSearchGenerator

app = Flask(__name__)
api = Api(app)
wg = WordSearchGenerator(dim=10, words=[], color_words=False)


class Product(Resource):
    def get(self):
        return {"grid": wg.grid, "word_bank": wg.words}


api.add_resource(Product, "/")

if __name__ == "__main__":
    app.run(host="192.168.0.15", port=5000, debug=True)

