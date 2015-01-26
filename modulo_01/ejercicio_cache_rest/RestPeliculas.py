__author__ = 'Javier'

import requests
import sqlite3


class Database(object):

    def read_from_database(self, movie_name):
        conn = sqlite3.connect("movies")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE name = '"+movie_name+"';")
        raw_data = cursor.fetchone()
        conn.close()
        return raw_data

    def save_in_database(self, movie_data):
        print("Saving.....")
        conn = sqlite3.connect("movies")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies VALUES('"+movie_data['Title']+"','"+movie_data['Year']+"');")
        conn.commit()
        conn.close()


class RestMovies(object):

   def read_from_rest(self, movie_name):
       "http://www.omdbapi.com/?t=birdman"
       raw_data = requests.get("http://www.omdbapi.com/", params={'t':movie_name})
       movie_info = raw_data.json()
       return movie_info


class InfoPeliculas(object):

    def __init__(self, db, rest_service):
        self._db = db
        self._rest_service = rest_service

    def recover_movie(self, movie_name):
        movie_info = self._db.read_from_database(movie_name)
        if movie_info == None:
            movie_info = self._rest_service.read_from_rest(movie_name)
            self._db.save_in_database(movie_info)
        return movie_info



if __name__ == "__main__":
    print("Running")
    info = InfoPeliculas(Database(), RestMovies())
    movie = info.recover_movie("No_existe")
    print(movie)
    print("ok")



