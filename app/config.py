from distutils.debug import DEBUG


class Config:
    '''
    parent configuration with general configurations
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    

class ProdConfig(Config):
    '''
    Production configuration class
    Args:
        Inherits general configurations from parent class Config
    '''
    pass
class DevConfig(Config):
    '''
    Development Configuration inherits from parent class
    '''
    DEBUG = True
    