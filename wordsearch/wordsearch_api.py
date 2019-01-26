from flask import Flask
from flask_restful import Resource, Api
from wordsearch_generator import WordSearchGenerator
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

icors = CORS(app, resources={r"/": {"origins": "*"}})


class Product(Resource):
    def get(self, dim):
        wg = WordSearchGenerator(dim)
        return {"grid": wg.grid, "word_bank": wg.words}


api.add_resource(Product, "/")

if __name__ == "__main__":
    app.run(host="192.168.0.18", port=5000, debug=True)
