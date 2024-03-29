import os

# Generate a random secret key.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = "postgres://{}@{}/{}".format(
    "reem", '127.0.0.1:5432', "fyyur")
SQLALCHEMY_TRACK_MODIFICATIONS = True


