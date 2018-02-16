'''fresh_tomatoes file should be in same folder'''
import fresh_tomatoes
import media

'''Instance of class Movie'''
a = "https://upload.wikimedia.org/wikipedia/en/6/69/"
toy_story = media.Movie(
            "Toy Story 3",
            "A story of a boy and his toy that come to life",
            a+"Toy_Story_3_poster.jpg",
            "https://www.youtube.com/watch?v=ZZv1vki4ou4")
b = "https://upload.wikimedia.org/wikipedia/en/b/b0/"
avatar = media.Movie(
        "Avatar",
        "A marine on an alien planet",
        b+"Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
c = "A retired hitman grieving the loss of his wife,"
d = "https://upload.wikimedia.org/wikipedia/en/9/98/"
john_wick = media.Movie(
            "John Wick",
            c+"is forced to return to his old ways.",
            d+"John_Wick_TeaserPoster.jpg",
            "https://www.youtube.com/watch?v=RllJtOw0USI")
e = "For a bachelor party,"
f = "https://upload.wikimedia.org/wikipedia/en/b/b9/"
hangover = media.Movie(
           "Hangover",
           e+" three best men and the groom take a road trip to Las Vegas.",
           f+"Hangoverposter09.jpg",
           "https://www.youtube.com/watch?v=tcdUhdOlz9M&t=30s")
g = "A woman's strength and thinking power grow exponentially"
h = "https://upload.wikimedia.org/wikipedia/en/1/14/"
lucy = media.Movie(
       "Lucy",
       g+"after the effects of a performance-enhancing drug set in.",
       h+"Lucy_%282014_film%29_poster.jpg",
       "https://www.youtube.com/watch?v=MVt32qoyhi0")
i = "Two small-time gun dealers, make it big when they find themselves "
j = "https://upload.wikimedia.org/wikipedia/en/5/52/"
war_dogs = media.Movie(
           "War Dogs",
           i+"landing a $300 million contract from the American government.",
           j+"War_Dogs_2016_poster.jpg",
           "https://www.youtube.com/watch?v=Rwh9c_E3dJk")
k = "Mark Watney is stranded on the planet of Mars after his crew leaves"
l = "https://upload.wikimedia.org/wikipedia/en/c/cd/"
the_martian = media.Movie(
              "The Martian",
              k+" him behind, presuming him to be dead due to a storm.",
              l+"The_Martian_film_poster.jpg",
              "https://www.youtube.com/watch?v=Ue4PCI0NamI")
m = "Five year old Saroo gets lost on a train which takes him thousands of"
n = "https://upload.wikimedia.org/wikipedia/en/f/f0/"
lion = media.Movie(
       "Lion",
       m+" miles across India, away from home and family.",
       n+"Lion_%282016_film%29.png",
       "https://www.youtube.com/watch?v=-RNI9o06vqo")
o = "The true story of Desmond Doss, who won the Congressional Medal of Honor"
p = "https://upload.wikimedia.org/wikipedia/en/8/8a/"
hacksaw = media.Movie(
          "Hacksaw Ridge",
          o+"despite refusing to bear arms during WWII on religious grounds.",
          p+"Hacksaw_Ridge_poster.png",
          "https://www.youtube.com/watch?v=s2-1hz1juBI")
'''storing movies instances in array'''
movies = [
         toy_story, avatar, john_wick, hangover, lucy, war_dogs, the_martian,
         lion, hacksaw]

'''Calling movie page'''
fresh_tomatoes.open_movies_page(movies)
