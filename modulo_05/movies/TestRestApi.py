__author__ = 'Javier'

import unittest
from movies.RESTApi import RestCache, MongoDBMoviesCache, ApiRest
import mongomock
import httpretty


class JsonCapturer(object):
    def capture(self, doc):
        self.doc = doc


class TestRestApi_UsingMongoMock(unittest.TestCase):

    def setUp(self):
        self.mongo_client = mongomock.MongoClient()

    def test_store_movies_in_cache(self):
        mockApiRest = ApiRest()
        cache = MongoDBMoviesCache(self.mongo_client)

        restCache = RestCache(mockApiRest, cache)
        restCache.search_movie("Sunshine")

        self.assertMovieInCache("Sunshine")

    def test_recover_movies_from_cache(self):
        mockApiRest = None
        cache = MongoDBMoviesCache(self.mongo_client)
        self.setMovieInCache({"Title":"Sunshine", "Year": "2007"})

        restCache = RestCache(mockApiRest, cache)
        restCache.search_movie("Sunshine")

    def assertMovieInCache(self, movie):
        self.assertIsNotNone(self.mongo_client.movies.movies.find_one({'Title': movie}))

    def setMovieInCache(self, movie_json):
        id = self.mongo_client.movies.movies.insert(movie_json)
        self.assertIsNotNone(id)


class TestRestApi_UsingHTTPretty(unittest.TestCase):

    @httpretty.activate
    def test_intercepting_url(self):
        httpretty.register_uri(httpretty.GET, "http://www.omdbapi.com/",
                           body='{"Title": "Demo movie", "Date": "2014"}',
                           content_type="application/json")

        apiRest = ApiRest()
        mongo_client = mongomock.MongoClient()
        cache = MongoDBMoviesCache(mongo_client)

        capturer = JsonCapturer()

        restCache = RestCache(apiRest, cache)
        restCache.show = capturer.capture
        restCache.search_movie("aliens")

        self.assertEqual(capturer.doc['Title'], "Demo movie")



if __name__ == '__main__':
    unittest.main()
