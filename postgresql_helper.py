import psycopg2
from fake_passager_entity import FakePassager
from fake_data_maker import FakeDataMake
import time


class PostgreDBHelper:
    def __init__(self):
        pass

    def get_DB_conn(self, host):

        conn = psycopg2.connect(database="postgres", user="postgres",
                                password="nuctech@beijing", host=host, port="5432")
        return conn

    def select(self, conn):
        fdm = FakeDataMake()
        psg = fdm.get_passager()
        connect = self.get_DB_conn(conn)
        cursor = connect.cursor()
        result = cursor.execute('select * from {}.{}'.format('DBTest', 'DBTest'))

    def add_fake_passager(self):
        try:
            count = 1
            total_last_time = time.time()
            fdm = FakeDataMake()
            while count <= 10000:
                psg = fdm.get_passager()
                conn = self.get_DB_conn('172.16.184.5')
                cursor = conn.cursor()

                input_value1 = "test for insert attribute1"
                input_value2 = "test for insert attribute2"

                # cursor.execute("select * from testtable")
                # rows = cursor.fetchall()

                result_insert = cursor.execute(
                    "INSERT INTO passenger_master(paperstype, papersnumber, nationality, name, gender, birthdate, birthplace) VALUES ('" + paperstype + "', '" + papersnumber + "', '" + nationality + "', '" + name + "', '" + gender + "', '" + birthdate + "' ,'" + birhplace + "' )")
                result_insert = conn.commit()
                current_time = time.time()

                print('')
                print('------------------------------------')
                print('Order: ' + str(count))
                print('Fake Passager: ' + str(fake_passager.__dict__))
                print("Time Consuming： {}".format(current_time - last_time))
                print('------------------------------------')
                print('')
                count = count + 1
                # print(rows)
            total_current_time = time.time()
            print('')
            print('------------------------------------')
            print("Total Time Consuming： {}".format(total_current_time - total_last_time))
            print('------------------------------------')
            print('')
        except Exception as e:
            print('')
            print('------------------------------------')
            print("Total Time Consuming： {}".format(total_current_time - total_last_time))
            print('------------------------------------')
            print('')
            print(e)
