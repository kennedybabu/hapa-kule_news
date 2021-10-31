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

        self.new_news = News('Sudan coup: Three killed in protests against military takeover','Here we go', 'https://ichef.bbci.co.uk/news/1024/branded_news/184F9/production/_121277599_mediaitem121277598.jpg', 'whistleBlower', '2021-10-31', '"http://www.bbc.co.uk/news/world-africa-59103901')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        '''
        Test if the News object is initialises properly
        '''
        self.assertEqual(self.new_news.title, "Sudan coup: Three killed in protests against military takeover")
        self.assertEqual(self.new_news.description, "Here we go")
        self.assertEqual(self.new_news.image, "https://ichef.bbci.co.uk/news/1024/branded_news/184F9/production/_121277599_mediaitem121277598.jpg")
        self.assertEqual(self.new_news.author, "whistleBlower")
        self.assertEqual(self.new_news.date_created, "2021-10-31")
        self.assertEqual(self.new_news.link, '"http://www.bbc.co.uk/news/world-africa-59103901')


if __name__ == '__main__':
    unittest.main()