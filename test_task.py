import unittest
import psycopg2
import datetime


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """connect to database"""
        self.conn = psycopg2.connect(dbname="Employee",
                        user="postgres",
                        host="localhost",
                        password="root",
                        port="5432")
        print("this is setup function")

    def tearDown(self):
        """Close the database"""
        self.conn.close()
        print("this is teardown class")


    def test_query(self):
        test_row = (7369, 'SMITH', 'CLERK', 7902, datetime.date(1980, 12, 17), 800.00, None, 20)
        cursor = self.conn.cursor()
        cursor.execute("select * from emp")
        row = cursor.fetchone()
        self.assertEqual(row,test_row)

if __name__ == "__main__":
    unittest.main()