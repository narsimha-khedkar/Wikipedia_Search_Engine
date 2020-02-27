from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, JSONEncoder
from flask_jsonpify import jsonify, jsonpify
from flask_cors import CORS
import wikipedia
import sys
from pdfminer.high_level import extract_text
from werkzeug import secure_filename
import os

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

# GET routes
api.add_resource(PerformQuery, '/query/<queryString>')

@app.route('/getArticle/<string:articleName>', methods=['GET'])
def get_article(articleName):
    if request.method == 'GET':
        try:
            article =  wikipedia.page(articleName)
            encodedArticle = MyEncoder().encode(article)
            return encodedArticle
        except wikipedia.DisambiguationError as e:
            # occurs when the wikipedia search returns a disambiguation page (a page with a list of multiple related articles)
            # capture this, then return one of them. Might offer some special functionality later on to allow the user to choose
            firstOption = e.options[0]
            nonAmbiguationArticle = wikipedia.page(firstOption)
            encodedArticle = MyEncoder().encode(nonAmbiguationArticle)
            return encodedArticle
        except Exception as e:
            print("Unexpected error", e)
            return e

# POST routes
@app.route('/uploadpdf', methods=['POST'])
def uploadpdf():
    if request.method == 'POST':
        try:
            file = request.files['fileKey']
            fileName = secure_filename(file.filename)
            file.save(fileName)

            text = extract_text(fileName)

            os.remove(fileName)

            return MyEncoder().encode("File received on API server.")
        except Exception as e:
            print("Unexpected error", e)
            return e


if __name__ == '__main__':
     app.run(port='5002')