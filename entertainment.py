
#import the media module with contains the Movie class
import media
#fresh_tomatoes enble us to generate our web page
import fresh_tomatoes
#create instances form movie class for every movie and it take 6 arguments
  # 1-movie_title  2-movie_storyline  3-poster_image  4-trailer_youtube  5-rate 6-The instance itself

  #Minions
Minions = media.Movie("MINIONS(2015)",
                      "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill,"+
                        "a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://www.youtube.com/watch?v=7AFUch5JZaQ",
                        "6.4/10")
  #Kung_Fu_Panda

Kung_Fu_Panda  = media.Movie("Kung Fu Panda",
                      "Kung Fu Panda is a 2008 American computer-animated action comedy martial arts film produced by DreamWorks Animation ",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg",
                      "https://www.youtube.com/watch?v=PXi3Mv6KMzY",
                         "7.6/10")
#avatar
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                        "7.8/10")
#toy_story
toy_story = media.Movie("Toy Story",
                           "A story of a boy and his toys that come to life",
                           "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                           "8.3/10")
#The_Adventures_of_Tintin
The_Adventures_of_Tintin=media.Movie("The Adventures of Tintin (2011)",
                          "Intrepid reporter Tintin and Captain Haddock set off on a treasure hunt for a sunken ship commanded by Haddock's ancestor. ",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/The_Adventures_of_Tintin_-_Secret_of_the_Unicorn.jpg/220px-The_Adventures_of_Tintin_-_Secret_of_the_Unicorn.jpg",
                          "https://www.youtube.com/watch?v=9ua_4ajpP58",
                          " 7.4/10")

#The_Lego_Batman_Movie
The_Lego_Batman_Movie=media.Movie("The Lego Batman Movie",
                                  "There are big changes brewing in Gotham, but if Batman (Will Arnett) wants to save the city ",
                                  "https://upload.wikimedia.org/wikipedia/en/6/61/The_Lego_Batman_Movie_PromotionalPoster.jpg",
                                  "https://www.youtube.com/watch?v=_pc2-y8WJn8",

                                  " 7.7/10 ")
#Moana
Moana = media.Movie("Moana (2016)",
                      "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous Chieftain's daughter's island,,",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser_Poster.jpg",
                      "https://www.youtube.com/watch?v=LKFuXETZUsI",
                        "7.8/10")


# Add  all movie objects created to a movies (array) and pass it to fresh_tomatoes to open web page 

movies=[Minions,Kung_Fu_Panda,avatar,toy_story,The_Adventures_of_Tintin,The_Lego_Batman_Movie,Moana]


# create and open the web page in a browser
fresh_tomatoes.open_movies_page(movies)
