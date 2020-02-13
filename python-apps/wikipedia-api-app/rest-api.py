from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, JSONEncoder
from flask_jsonpify import jsonify
from flask_cors import CORS
import wikipedia


app = Flask(__name__)
CORS(app)
api = Api(app)

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class SearchResult:
    ArticleName = ""
    ArticleContent = ""

class PerformQuery(Resource):
    def get(self, queryString):
        results = wikipedia.search(queryString)
        return results

class GetArticle(Resource):
    def get(self, articleName):
        article =  wikipedia.page(articleName)
        encodedArticle = MyEncoder().encode(article)
        return encodedArticle

api.add_resource(PerformQuery, '/query/<queryString>')
api.add_resource(GetArticle, '/getArticle/<articleName>')

if __name__ == '__main__':
     app.run(port='5002')