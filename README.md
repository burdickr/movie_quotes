# Movie Quote Generator App

[Check out the movie quote generator running here!](https://ryan-movie-quotes.herokuapp.com/)

* This app will take a randomized movie title from a csv file and scrape rotten tomatoes for quotes from the movie.

* You can also type in a movie title to search for specified quotes. 

* The app was created as a quick way to generate random quotes for trivia. On my team at work we use this app to send each other a random movie quote in the morning and then it's a mini competition to see who can guess correctly first. 

* There are some limitiations due to rotten tomatoes having some movie titles stored with additional numbers or characters that are not truly part of the movie title. When those instances occur no movie quotes will be displayed but there is a link available at the top of the page to search google for quotes with the randomized movie title. 

* Although this app has ultimately a silly purpose the way it is designed and the function used primarily in Python can be applied to more important issues and finding relevent information from across the web based on a users request. 

### Steps to duplicate this app 

1. Visit Kaggle to download a CSV containing movie titles. 

2. Use python packages to create a dataframe containing just the movie titles. Optionally you can filter out less popular movies to make the returned quotes more recognizable. 

3. Create a backend app in python that uses the web scraping function to return the necessary data to plug into the front end. 

4. Create a front end application that allows the user to implement the webscrapping feature at the click of a button.