import requests
from bs4 import BeautifulSoup
import pandas as pd
movies = pd.read_csv('movies_data.csv')

# Set scrape function
def scrape_quote():
    movies = pd.read_csv('movies_data.csv')
    clean_movies_df = pd.DataFrame(movies)
    clean_movies_df.drop(clean_movies_df.loc[clean_movies_df['popularity']<30].index, inplace=True)
    most_popular_df = clean_movies_df.sort_values(by=["popularity"], ascending=False)
    random_movie = most_popular_df.sample()
    use_movie = random_movie.sample()
    title = use_movie["title"].values[0]
    term = use_movie["title"].values[0].replace(" " or ":", "_")
    url = "https://www.rottentomatoes.com/m/" + term + "/quotes/"
    url2 = "https://www.google.com.tr/search?q={}".format(title) +" movie quotes"
    # Get the html from a request to the url
    response = requests.get(url)
    html = response.text
    # Convert the html into a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    # Get all info from the specified .find_all() location
    quotes = soup.find_all('li', class_='quote_item')
    all_quotes = []
    for quote in quotes:
        info = quote.text
        info_dict = {'info': info}
        all_quotes.append(info_dict)
        # Return links as a dictionary value 
    return {
        'url2': url2, 
        'title': title, 
        'all_quotes': all_quotes
    }

    

