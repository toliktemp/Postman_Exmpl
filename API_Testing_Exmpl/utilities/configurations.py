import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("/Users/tolik/PycharmProjects/Project_API_Example/utilities/properties.ini")
    return config
