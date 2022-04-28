class Movie:
    '''
    Movie class to define movie objects
    '''
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count


        '''
        1. Title - The name of the movie
        2. Overview - A short desc of the movie
        3. poster - Poster image of the movie
        4. vote_average - Average rating of the movie
        5. vote_count - How many people have rated the movie
        6. id - The movie ID

        '''