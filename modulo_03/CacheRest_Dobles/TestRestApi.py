__author__ = 'Javier'

import unittest
from unittest.mock import MagicMock
from movies.RESTApi import RestCache
from mockito import mock, when, verify

class TestRestApi_UsingMagicMock(unittest.TestCase):

    def test_recovering_movies_from_cache(self):
        mockApiRest = MagicMock()
        mockCache = MagicMock()
        mockCache.search = MagicMock(return_value={'Title':"Sunshine", 'Year':"2007"})
        restCache = RestCache(mockApiRest, mockCache)

        restCache.search_movie("Sunshine")

        assert mockApiRest.search.call_count == 0

    def test_recovering_movies_from_api(self):
        mockApiRest = MagicMock()
        mockCache = MagicMock()
        mockCache.search = MagicMock(return_value=None)
        restCache = RestCache(mockApiRest, mockCache)

        restCache.search_movie("Sunshine")

        mockApiRest.search.assert_called_once_with("Sunshine")



class TestRestApi_UsingMockito(unittest.TestCase):

    def test_recovering_movies_from_cache(self):
        mockApiRest = mock()
        mockCache = mock()
        when(mockCache).search("Sunshine").thenReturn({'Title':"Sunshine", 'Year':"2007"})

        restCache = RestCache(mockApiRest, mockCache)
        restCache.search_movie("Sunshine")

        verify(mockCache, 1).search("Sunshine")
        verify(mockApiRest, 0).search("Sunshine")

    def test_recovering_movies_from_api(self):
        mockApiRest = mock()
        mockCache = mock()
        when(mockCache).search("Sunshine").thenReturn(None)

        restCache = RestCache(mockApiRest, mockCache)
        restCache.search_movie("Sunshine")

        verify(mockApiRest, 1).search("Sunshine")


if __name__ == '__main__':
    unittest.main()
