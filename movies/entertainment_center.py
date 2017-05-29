import media
import fresh_tomatoes
lost_in_translation = media.Movie("Lost in translation",
                        "A faded movie star and a neglected young woman form an unlikely bond after crossing paths in Tokyo. ",
                        "https://s-media-cache-ak0.pinimg.com/originals/27/54/d8/2754d819bb6cb4a9787bb8a25bf09564.jpg",
                        "https://www.youtube.com/watch?v=W6iVPCRflQM&t=11s")

reservoir_dogs = media.Movie("Reservoir Dogs", 
              "Storyline", 
              "https://www.movieposter.com/posters/archive/main/12/A70-6021", 
              "https://www.youtube.com/watch?v=GLPJSmUHZvU")

alien = media.Movie(
  "Alien",
  "Storyline",
  "http://www.impawards.com/1979/posters/alien.jpg",
  "https://www.youtube.com/watch?v=LjLamj-b0I8")


transpotting = media.Movie("Transpotting",
                     "Renton, deeply immersed in the Edinburgh drug scene,"
                     "tries to clean up and get out, despite the allure of the drugs and influence of friends.",
                     "http://img.goldposter.com/2015/04/Trainspotting_poster_goldposter_com_9.jpg",
                     "https://www.youtube.com/watch?v=8LuxOYIpu-I")

metropolis  = media.Movie("Metropolis",
                                "In a futuristic city sharply divided between the working class and the city planners"
                               "the son of the city's mastermind falls in love with a working class"
                               "prophet who predicts the coming of a savior to mediate their differences. ",
                                "https://store-media.nytimes.com/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/3/03466us02.jpg",
                                "https://www.youtube.com/watch?v=GrFBId1b8U0")

her = media.Movie("Her",
                          "A lonely writer develops an unlikely relationship with an operating system designed to meet his every need. ",
                          "http://www.newdvdreleasedates.com/images/posters/large/her-2013-10.jpg",
                          "https://www.youtube.com/watch?v=ne6p6MfLBxc")
spaceOdyssey = media.Movie("2001: A Space Odyssey",
                                "storyline",
                                "http://www.fatmovieguy.com/wp-content/uploads/2014/12/2001-A-Space-Odyssey-Movie-Poster.png",
                                "https://www.youtube.com/watch?v=Z2UWOeBcsJI"
                                )
ex_machina = media.Movie("Ex Machina",
                           "A young programmer is selected to participate in a ground-breaking"
                          "experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I. ",
                           "https://s-media-cache-ak0.pinimg.com/originals/5d/9f/92/5d9f923f3e51fc0d6cd54a1e60b1f86e.jpg",
                           "https://www.youtube.com/watch?v=gyKqHOgMi4g")

coherence = media.Movie("Coherence",
  "storyline",
  "http://www.impawards.com/2014/posters/coherence_xlg.jpg",
  "https://www.youtube.com/watch?v=kxAOewNzz-8")

Paprika = media.Movie("Paprika",
  "storyline",
  "http://img.moviepostershop.com/paprika-movie-poster-2006-1020689313.jpg",
  "https://www.youtube.com/watch?v=jJzEW_eE1G0")

movies = [lost_in_translation, reservoir_dogs，alien, transpotting, metropolis, her, spaceOdyssey, ex_machina, coherence, Paprika]
#this is the list of the movie instances

fresh_tomatoes.open_movies_page(movies)
#This function call uses list of movie instances as input to generate and HTML file
#and open it in the browser
