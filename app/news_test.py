import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''

        self.new_news = News(12, 'Here we go', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 'whistleBlower', '2021-10-31')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        '''
        Test if the News object is initialises properly
        '''
        self.assertEqual(self.new_news.description, "Here we go")
        self.assertEqual(self.new_news.image, "https://image.tmdb.org/t/p/w500/khsjha27hbs")
        self.assertEqual(self.new_news.author, "whistleBlower")
        self.assertEqual(self.new_news.date_created, "2021-10-31")


if __name__ == '__main__':
    unittest.main()