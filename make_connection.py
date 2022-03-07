import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging


class make_connection_to_postgresql:
    def make_connection_to_db(self):
        conn_string = "host='localhost' dbname='Employee' user='postgres' password='root'"

        # print the connection string we will use to connect
        # print "Connecting to database\n	->%s" % (conn_string)
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        return cursor
if __name__ == "__main__":
  obj=make_connection_to_postgresql()
  cursor = obj.make_connection_to_db()
# task1(cursor)


