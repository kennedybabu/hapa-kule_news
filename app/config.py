class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category=general&language=en&pageSize=30&apiKey={}'
    # https://newsapi.org/v2/everything?q=Apple&from=2021-10-31&sortBy=popularity&apiKey=API_KEY



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True