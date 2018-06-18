import unittest
from app.models import Sources


class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.sources = Sources(1234, 'Amazing news', 'Thrilling news', 'https://abcnews.go.com', 'Technology',
                             'UnitedStates', 'English')

    def test_instance(self):
        self.assertTrue(isinstance(self.sources, Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.sources.id, 'wired')
        self.assertEquals(self.sources.name, 'wired News')
        self.assertEquals(self.sources.description, 'tech news provider')
        self.assertEquals(self.sources.url, 'wired.com')
        self.assertEquals(self.sources.category, 'tech')
        self.assertEquals(self.sources.country, 'U.S.A')
        self.assertEquals(self.sources.language, 'en')
