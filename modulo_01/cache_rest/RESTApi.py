__author__ = 'Javier'

import sqlite3
import urllib.request
import json


class SQLLiteMoviesCache(object):

    # TIP: evita codigo duplicado
    def search(self, movie_name):
        conn = sqlite3.connect('movies')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE name = '"+movie_name+"';")
        raw_movie = cursor.fetchone()
        return raw_movie

    def store(self, movie):
        conn = sqlite3.connect('movies')
        cursor = conn.cursor()
        query = "INSERT INTO movies VALUES('"+movie['Title']+"','"+movie['Year']+"');"
        cursor.execute(query)
        conn.commit()


class ApiRest(object):

    # TIP: usa la librería Request
    def search(self, movie_name):
        url = "http://www.omdbapi.com/?t="+movie_name
        connection = urllib.request.urlopen(url)
        result_raw = connection.read().decode('utf-8')
        raw_movie = json.loads(result_raw)
        return raw_movie


class RestCache(object):

    # TIP: encapsula la información de la película
    def search_movie(self, movie_name):
        cache = SQLLiteMoviesCache()
        api_rest = ApiRest()

        movie = cache.search(movie_name)
        # TIP: implementa nillpointerpattern
        if movie is None:
            print("Movie not in cache.")
            movie = api_rest.search(movie_name)
            cache.store(movie)
        self.show(movie)

    def show(self, movie):
        print(movie)


if __name__ == "__main__":
    cache = RestCache()
    cache.search_movie("Her")