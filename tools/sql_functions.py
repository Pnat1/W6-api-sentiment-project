from numpy import record
import pandas as pd
import ast
import string
import os
import dotenv
import sqlalchemy as alch
dotenv.load_dotenv()

sql_pass = os.getenv("sql_pass")
dbName = "pulp_fiction_dialogue"
data_connection = f"mysql+pymysql://root:{sql_pass}@localhost/{dbName}"
engine = alch.create_engine(data_connection)
print("Connection Completed")




def actor_characters():
    """
    Calls the database in MySQl and returns all the actor characters in a json format.
    """
    query = f"""
    SELECT film_character FROM actors;
    """
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")


def lines():
    """
    Calls the database in MySQl and returns all the script lines in a json format.
    """
    query= f"""
    SELECT line_quote FROM line_quotes;
    """
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")


def places():
    """
    Calls the database in MySQl and returns the different places where the film_characters 
    said their lines.
    """
    query = f"""
    SELECT place FROM place;
    """
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient='records')


def actor_line(actor_name):
    """
    You can put the name of the author you want and this returns his name, the palce
    he is in and the script line he says.
    """
    query = f"""
    SELECT film_character, line_quote, place
    FROM actors
    INNER JOIN line_quote ON actors_actor_id = actor_id
    INNER JOIN place ON place_id = place_place_id 
    WHERE actor_name = '{film_character}';
    """
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")