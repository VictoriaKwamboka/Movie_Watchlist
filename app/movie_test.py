import unittest
# from app.models.movie import Movie
from models import movie 
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the movie class
    '''
    def setUp(self):
        '''
        Set up method that runs before every test
        '''
        self.Movie(1234, 'Python Must Be Crazy', 'A Thrilling new Python Series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == '__main__':
    unittest.main()
