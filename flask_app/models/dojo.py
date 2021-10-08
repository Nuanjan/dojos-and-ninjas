# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Now we use class methods to query our database

        self.ninja = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        # will return the id of that data that we just insert in
        return connectToMySQL('dojos_ninjas').query_db(query, data)

    @classmethod
    def get_dojo_with_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo = cls(results[0])
        print(results)
        for ninja_row in results:
            ninja_data = {
                "id": ninja_row['ninjas.id'],
                "first_name": ninja_row['first_name'],
                "last_name": ninja_row['last_name'],
                "age": ninja_row['age'],
                "dojo_id": ninja_row['dojo_id'],
                "created_at": ninja_row['ninjas.created_at'],
                "updated_at": ninja_row['ninjas.updated_at']
            }
            dojo.ninja.append(ninja.Ninja(ninja_data))
        return dojo
