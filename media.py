import webbrowser

class Movie():
        """A Class that stores data about a movie."""
        # instance variables
	def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	#instance methods
	#a function to open a webbrowser page to the movie's youtube trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

