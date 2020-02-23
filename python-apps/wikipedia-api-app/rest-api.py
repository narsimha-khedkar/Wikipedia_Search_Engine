from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, JSONEncoder
from flask_jsonpify import jsonify, jsonpify
from flask_cors import CORS
import wikipedia
import sys

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

# GET routes
api.add_resource(PerformQuery, '/query/<queryString>')
api.add_resource(GetArticle, '/getArticle/<articleName>')

# POST routes
@app.route('/uploadpdf', methods=['POST'])
def uploadpdf():
    if request.method == 'POST':
        try:
            file = request.files['fileKey']
            encodedFileData = MyEncoder().encode(file)
            return encodedFileData
        except Exception as e:
            print("Unexpected error", e)


if __name__ == '__main__':
     app.run(port='5002')