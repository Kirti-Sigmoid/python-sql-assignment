import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging
class Task4:
    def task4(self):
        with pd.ExcelFile("../task2.xlsx") as xls:
            df = pd.read_excel(xls)

        gk = df.groupby('dname').agg({"total_compensation": sum}).reset_index().rename(
            columns={"deptno": "Dept No", "dname": "Dept Name", "total_compensation": "Compensation"})
        gk.to_excel("/Users/kirti_sigmoid/PycharmProjects/python-sql-assignment/task4.xlsx", header=True, index=False)
        print(gk)

if __name__ == "__main__":

    obj_task=Task4()
    obj_task.task4()

