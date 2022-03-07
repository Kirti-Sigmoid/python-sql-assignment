import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging
from make_connection import make_connection_to_postgresql

# task2
# Write a python program to list the Total compensation  given till his/her last date or
# till now of all the employees till date in a xlsx file.
# columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization
class Task2:
    def task2(self,cursor):
        # update the end date to current date to find the month spent of each employee who are in the orgenisation
        update_end_date = "update jobhist set enddate=current_date where enddate=null"
        try:
            cursor.execute(update_end_date)  # this will execute the query
            logging.debug(f" updation executed on cursor - {cursor}")
        except:
            logging.error("failed to fetch ci=ursor from database")

        query = "select emp.ename,emp.empno,dept.deptno, dept.dname,round((jh.enddate - jh.startdate)/30)*jh.sal as total_compensation," \
                "date_part('month',age(jh.enddate, jh.startdate)) as " \
                "emp_month_spent from emp join dept on emp.deptno = dept.deptno join jobhist as jh on emp.empno = jh.empno"
        try:
            cursor.execute(query)  # this will execute the query
            logging.debug(f" query executed on cursor - {cursor}")
        except:
            logging.error("failed to fetch ci=ursor from database")
            # extracting all data from cursor
        query_result = cursor.fetchall()

        # print(query_result)

        # inserting header in query result
        query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])

        # creating dataframe from data (list_type)
        df = pd.DataFrame(query_result)
        try:
            path = "/task2.xlsx"
            # adding data to excel file
            df.to_excel(path, header=False, index=False)
            logging.info(f"Dataframe converted to excel stored in location -{path}")
        except:
            logging.error(f"Unable to convert dataframe to excel in location - {path}")


if __name__ == "__main__":
    obj = make_connection_to_postgresql()
    cursor = obj.make_connection_to_db()
    obj_task=Task2()
    obj_task.task2(cursor)




