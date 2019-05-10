# Set up app
from flask import Flask, render_template, redirect
import os, movie_scrape

app = Flask(__name__)

# Create route
@app.route('/')
def home():
    movies = movie_scrape.scrape_quote()
    # Render the info in links to the html file
    return render_template('index.html', movies=movies)

#local testing
#if __name__ == "__main__":
  # app.run(debug=True)
# Define port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)