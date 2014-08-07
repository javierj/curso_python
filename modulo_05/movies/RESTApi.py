__author__ = 'Javier'

import sqlite3
import urllib.request
import json
import pymongo

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


class MongoDBMoviesCache(object):

    def __init__(self, mongo_con = None):
        if mongo_con == None:
            self.conn = pymongo.MongoClient()
        else:
            self.conn = mongo_con

    # TIP: evita codigo duplicado
    def search(self, movie_name):
        db = self.conn['movies']
        movies_col = db['movies']
        movie = movies_col.find_one({"Title":movie_name})
        return movie

    def store(self, movie):
        db = self.conn['movies']
        movies_col = db['movies']
        movie = movies_col.insert(movie)


class ApiRest(object):

    # TIP: usa la librería Request
    def search(self, movie_name):
        url = "http://www.omdbapi.com/?t="+movie_name
        connection = urllib.request.urlopen(url)
        result_raw = connection.read().decode('utf-8')
        raw_movie = json.loads(result_raw)
        return raw_movie


class RestCache(object):

    def __init__(self, apirest, moviecache):
        self._apirest = apirest
        self._moviecache = moviecache

    # TIP: encapsula la información de la película
    def search_movie(self, movie_name):
        movie = self._moviecache.search(movie_name)
        # TIP: implementa nillpointerpattern
        if movie is None:
            print("Movie not in cache.")
            movie = self._apirest.search(movie_name)
            self._moviecache.store(movie)
        self.show(movie)

    def show(self, movie):
        print(movie)


if __name__ == "__main__":
    cache = RestCache(ApiRest(), MongoDBMoviesCache())
    movie = cache.search_movie("Alien")
