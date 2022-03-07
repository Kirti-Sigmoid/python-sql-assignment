import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging
from make_connection import make_connection_to_postgresql


class Task3:
    def task3(self,cursor):
        try:
            engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Employee")
            print(engine)
            logging.debug(f"Successfully create engine  - {engine}")
        except:
            logging.error("failed to create engine")

        with pd.ExcelFile("../task2.xlsx") as xls:
            df = pd.read_excel(xls)
            try:
                df.to_sql(name="task2_table", con=engine, if_exists="replace", index=False)
                logging.debug("table is created from the excel file and data successfulyy uploaded")
            except:
                logging.debug("Exception occurred while uploading data to table")
        query = "select * from task2_table"
        cursor.execute(query)
        query_result = cursor.fetchall()
        print(query_result)


# Read and upload the above xlsx in 2) into a new table in the Postgres DB

if __name__ == "__main__":
    obj=make_connection_to_postgresql()
    cursor = obj.make_connection_to_db()
    obj_task = Task3()
    obj_task.task3(cursor)

