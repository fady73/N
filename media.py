# Project: Udacity:Programming Foundations with Python:MovieTrailer

import webbrowser
#enable us to open browser

class Movie():
#Constructor:
           # Parameters: movie_title,movie_storyline , poster_image, trailer_youtube,rate
           # movie_title: The title of the movie
	   # movie_storyline: Short  description about story of movie
           # poster_image: A url to a image of the movie poster
           # trailer_youtube: A url to a youtube video for the movie trailer
	   # rate :A rate of movie in imdb
    def __init__(self,movie_title,movie_storyline,poster_image,
                trailer_youtube,rate):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.m_rate=rate
		
    #this function is call to open the browser and show the movie trailer
    def show_trailers(self):
        webbrowser.open( self.trailer_youtube_url)
