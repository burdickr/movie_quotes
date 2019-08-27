# Set up app
from flask import Flask, render_template, redirect, request
import os, movie_scrape


app = Flask(__name__)

# Create route
@app.route('/')
def home():
    movies = movie_scrape.scrape_quote()
    # Render the info in links to the html file
    return render_template('index.html', movies=movies)

@app.route('/title', methods=["GET", "POST"])
def search_movie():
    if request.method =="POST":
        movies = movie_scrape.selected_movie(request.form["movieSearch"]) 
        return render_template('index.html', movies=movies)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)