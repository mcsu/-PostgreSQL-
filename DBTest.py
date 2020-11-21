import psycopg2
from faker import Faker

import PostgreConfig
from fake_passager_entity import FakePassager
import random
import time


class DBTest:
    def __init__(self, host):
        try:
            print('连接数据库')
            self.conn = psycopg2.connect(database=PostgreConfig.DB_NAME, user=PostgreConfig.USER_NAME,
                                         password=PostgreConfig.PASSWORD, host=host,
                                         port=PostgreConfig.PORT)
            print('连接成功')
        except Exception as e:
            print(e)

    def fake_data_make(self):
        try:
            fake = Faker("zh_CN")
            fake_passager = FakePassager()
            fake_passager.paperstype = fake.bothify(text='?', letters="DP")
            fake_passager.papersnumber = fake.bothify(text='?########', letters="EMD")
            fake_passager.nationality = str(random.randint(1, 143))
            fake_passager.name = fake.last_romanized_name() + ' ' + fake.last_romanized_name()
            fake_passager.gender = fake.bothify(text='?', letters="FM")
            fake_passager.birthdate = fake.date()
            fake_passager.birthplace = fake.address()
            fake_passager.date = fake.date()
            return fake_passager
        except Exception:
            print("ERR")

    def close_db_connection(self):
        self.conn.commit()
        self.conn.close()

    def basic_select_operate(self, sql):  # SELECT * FROM wequarantine.caiyangitem_dict
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # cursor.execute("insert into people values (%s, %s)", (who, age)) wequarantine.caiyangitem_dict
        rows = cursor.fetchall()
        for row in rows:
            print('passport_type：', row[1], 'passport_number', row[2], ' nationality', row[3], 'name：', row[4],
                  ' gender', row[5], ' birth_date', row[6], 'birth_place：', row[7], '\n')
        self.close_db_connection()

    def basic_insert_operate(self, psg):  # SELECT * FROM wequarantine.caiyangitem_dict
        cursor = self.conn.cursor()
        cursor.execute('insert into "DBTest"."DBTest" ("PassportType", "PassportNumber", "Nationality", '
                       '"Name", "Gender", "BirthDate", "BirthPlace") values (%s, %s, %s, %s, %s, %s, %s)',
                       (psg.paperstype, psg.papersnumber, psg.nationality, psg.name, psg.gender, psg.birthdate
                        , psg.birthplace))
        # rows = cursor.fetchall()
        # for row in rows:
        #     print()
        # print(rows)
        # self.close_db_connection()

def test(db):
    print('开始测试')
    count = 10000
    wait = 0.000001
    time1 = time.time()
    for i in range(count):
        db.basic_insert_operate(db.fake_data_make())
        if i % 100 == 0:
            print(i / 100)
        time.sleep(wait)
    time2 = time.time()
    db.close_db_connection()
    print('结束')
    temp = time2 - time1 - count * wait
    print(temp)

# INSERT INTO "DBTest" ("PassportType", "PassportNumber", "Nationality", "Name", "Gender", "BirthDate", "BirthPlace") VALUES ('D', 'E92547208', '71', 'Yi Pei', 'F', '2015-08-16', ' 北京市宜都县崇文常街h座 577276');

# a.basic_select_operate('select * from "DBTest"."DBTest"')
docker = DBTest('172.16.184.5')
origin = DBTest('172.16.184.6')
if __name__ == '__main__':
    print('docker')
    test(docker)
    print('原生')
    test(origin)


