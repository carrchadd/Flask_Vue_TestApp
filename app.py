from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.get('/')
def index():
    return 'Hello, World!'

@app.get('/api/v1/movies')
def get_movies():
    return jsonify([{
        'title': 'The Shawshank Redemption',
        'year': 1994,
        'rating': 9.3
    }, {
        'title': 'The Godfather',
        'year': 1972,
        'rating': 9.2
    }, {
        'title': 'The Dark Knight',
        'year': 2008,
        'rating': 9.0
    }])