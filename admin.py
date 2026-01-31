from database import db, cs
from ui import header, menu, pause

def SCHEDULE_AIR():
    while True:
        AID=input('Flight ID: ').upper()
        cs.execute(f'SELECT * FROM AIRLINES WHERE AID="{AID}"')
        flight=cs.fetchone()
        if flight:
            print('Flight already exists')
        else:
            Date=input('Date[YYYY-MM-DD]: ')
            DLocation=input('Departure location: ').upper()
            ALocation=input('Arrival location: ').upper()
            DTime=input('Departure time[HH:MM:SS]: ')
            ATime=input('Arrival time[HH:MM:SS]: ')
            Fare=float(input('Fare(in Rs.): '))
            SQL=f'INSERT INTO AIRLINES VALUES("{AID}","{Date}","{DLocation}", "{ALocation}","{DTime}","{ATime}",{Fare})'
            cs.execute(SQL)
            db.commit()
            print('Flight Scheduled')
        print()
        K=input('More flights? [Y/N]: ')
        print()
        if K in 'nN':
                break

def EDIT_AIR():
    air_ID=input('Enter flight ID: ').upper()
    cs.execute(f'SELECT * FROM AIRLINES WHERE AID="{air_ID}"')
    flight=cs.fetchone()
    if not flight:
        print('No such flight')
    else:
        print("1:Date[YYYY-MM-DD]  2:Departure Location  3:Arrival Location  4:Departure Time[HH:MM:SS]  5:Arrival Time[HH:MM:SS]  6:Fare")
        while True:
            K=int(input("EDIT- "))
            if K<1 or K>6:
                print('Invalid option')
            elif K==6:
                new=int(input('Enter revised fare: '))
                sql=f"UPDATE AIRLINES set Fare={new} where AID='{air_ID}'"
                cs.execute(sql)
                db.commit()
            else:
                new=input('Enter revised detail: ')
                if K==1:                    
                    sql=f"UPDATE AIRLINES set Date='{new}' where AID= '{air_ID}'"
                elif K==2:
                    sql=f"UPDATE AIRLINES set DLocation='{new}' where AID= '{air_ID}'"
                elif K==3:
                    sql=f"UPDATE AIRLINES set ALocation='{new}' where AID= '{air_ID}'"
                elif K==4:
                    sql=f"UPDATE AIRLINES set DTime='{new}' where AID= '{air_ID}'"
                else:
                    sql=f"UPDATE AIRLINES set ATime='{new}' where AID= '{air_ID}'"
                cs.execute(sql)
                db.commit()
            print('Edit successful')
            ch=input('More changes in this flight?[Y/N]: ')
            if ch in 'nN':
                break

def DELETE_AIR():
    air_ID=input('Enter flight ID: ').upper()
    cs.execute(f'SELECT * FROM AIRLINES where AID="{air_ID}"')
    flight=cs.fetchone()
    if not flight:
        print('Invalid ID')
    else:
        cs.execute(f"DELETE FROM AIRLINES where AID='{air_ID}'")
        cs.execute(f"DELETE FROM BOOKINGS where AID='{air_ID}'")
        db.commit()
        print('Flight and all related bookings canceled')

def SHOW_BOOK_AIR():
    air_ID=input('Enter flight ID: ')
    cs.execute(f'SELECT * FROM AIRLINES where AID="{air_ID}"')
    flight=cs.fetchone()
    if not flight:
        print('Invalid ID')
    else:
        cs.execute(f"SELECT * FROM BOOKINGS where AID='{air_ID}'")
        T=cs.fetchall()
        if not T:
            print('No bookings made')
        else:
            print('Bookings for flight -',air_ID)
            print('------------------------------------------------')
            print('LoginID   Class      Adults  Children  Fare')
            print('------------------------------------------------')
            for i in T:
                if i[2]=='BUSINESS':
                    print(f"{i[0]}       {i[2]}     {i[3]}        {i[4]}     {i[5]}")
                else:
                    print(f"{i[0]}       {i[2]}      {i[3]}        {i[4]}     {i[5]}")
            print('------------------------------------------------')


def admin_menu():
    while True:
        header("ADMIN PANEL")

        menu({
            "S": "Schedule Flight",
            "E": "Edit Flight",
            "C": "Cancel Flight",
            "B": "View Bookings",
            "Q": "Logout"
        })

        ch = input("Option: ").upper()

        if ch == 'S':
            SCHEDULE_AIR()
        elif ch == 'E':
            EDIT_AIR()
        elif ch == 'C':
            DELETE_AIR()
        elif ch == 'B':
            SHOW_BOOK_AIR()
        elif ch == 'Q':
            break
        else:
            print("Invalid option")
            pause()
