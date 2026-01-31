import pymysql

from db_config import DB_HOST, DB_USER, DB_PASSWORD

db = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    port=3306
)

cs = db.cursor()
cs.execute("CREATE DATABASE IF NOT EXISTS AIRWAYS_DB")
cs.execute("USE AIRWAYS_DB")

try:
    cs.execute('CREATE TABLE PASSENGERS(PID int(5) Primary Key, PName varchar(25) Not Null, PGender varchar(10), PAge int(3), PEmail varchar(35) Unique)')
except:
    print('PASSENGERS DB exists')
    pass
else:
    print('PASSENGERS DB created')


try:
    cs.execute('CREATE TABLE AIRLINES(AID char(9) Primary Key, Date date, DLocation varchar(20), ALocation varchar(20), DTime time, ATime time, Fare float(9,2))')
except:
    print('AIRLINES DB exists')
    pass
else:
    print('AIRLINES DB created')

try:
    cs.execute('CREATE TABLE BOOKINGS(PID int(5), AID char(9), Class varchar(10), Adults int(1), Children int(1), TFare float(10,2))')
except:
    print('BOOKINGS DB exists')
    pass
else:
    print('BOOKINGS DB created')


