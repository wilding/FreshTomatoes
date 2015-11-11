import fresh_tomatoes
import media

# create 6 instances of the class Movie and specify values of instance variables
inglourious_basterds = media.Movie("Inglourious Basterds", "Killin Nazis", "http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg", "https://www.youtube.com/watch?v=6AtLlVNsuAc")
the_big_lebowski = media.Movie("The Big Lebowski", "The dude abides.", "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg", "https://www.youtube.com/watch?v=cd-go0oBF4Y")
house_of_flying_daggers = media.Movie("House of Flying Daggers", "", "http://upload.wikimedia.org/wikipedia/en/f/f7/House_of_Flying_Daggers_poster.JPG", "https://www.youtube.com/watch?v=-GLVaSYzAvg")
v_for_vendetta = media.Movie("V for Vendetta", "Remember, remember, the 5th of November.", "http://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg", "https://www.youtube.com/watch?v=lSA7mAHolAw")
inception = media.Movie("Inception", "BBBWWWWWAAAAAAHHHHHHHHHHHHHHHHHHHH", "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")
pirates = media.Movie("Pirates of the Carribean", "An adventurous search for more rum.", "http://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg", "https://www.youtube.com/watch?v=naQr0uTrH_s")

# create an array that contains all instances of class Movie
movies = [inglourious_basterds, the_big_lebowski, house_of_flying_daggers, v_for_vendetta, inception, pirates]
# use a function from fresh_tomatoes.py that takes in the array and opens a webpage of movie trailers
fresh_tomatoes.open_movies_page(movies)
