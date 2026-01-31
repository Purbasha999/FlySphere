from database import db, cs
from ui import header, menu, pause

def REGISTER_PASS():
    while True:
        PID=int(input('Set User ID: '))
        cs.execute(f'SELECT * FROM PASSENGERS WHERE PID={PID}')
        passenger=cs.fetchone()
        if passenger:
            print('ID exists')
        else:
            break
    PName=input('Name: ').upper()
    PGender=input('Gender: ').capitalize()
    PAge=int(input('Age: '))
    PEmail=input('Email ID: ')
    sql=f'Insert into PASSENGERS values({PID},"{PName}","{PGender}",{PAge}, "{PEmail}")'
    cs.execute(sql)
    db.commit()
    print('Sign Up successful') 


def SHOW_PASS():
    pass_ID=int(input('Enter Login ID: '))
    cs.execute(f'SELECT * FROM PASSENGERS where PID={pass_ID}')
    passenger=cs.fetchone()
    if not passenger:
        print('Invalid ID')
    else:
        print('ACCOUNT DETAILS:-')
        print('------------------')
        print('Login ID:',passenger[0])
        print('Name:', passenger[1])
        print('Gender:',passenger[2])
        print('Age:',passenger[3])
        print('Email:',passenger[4])
        return pass_ID


def EDIT_PASS(S):
    cs.execute(f'SELECT * FROM PASSENGERS where PID={S}')
    passenger=cs.fetchone()
    if not passenger:
        print('Invalid ID')
    else:
        print("1:Name  2:Gender  3:Age  4:Email")
        while True:
            K=int(input("EDIT- "))
            if K<1 or K>4:
                print('Invalid option')
            elif K==3:
                new=int(input('Enter revised age: '))
                sql=f"UPDATE PASSENGERS set PAge={new} where PID={S}"
                cs.execute(sql)
                db.commit()
            else:
                new=input('Enter revised detail: ')
                if K==1:                    
                    sql=f"UPDATE PASSENGERS set PName='{new}' where PID={S}"
                elif K==2:
                    sql=f"UPDATE PASSENGERS set PGender='{new}' where PID={S}"
                else:
                    sql=f"UPDATE PASSENGERS set PEmail='{new}' where PID={S}"
                cs.execute(sql)
                db.commit()
            print('Edit successful')
            ch=input('More changes in this account?[Y/N]: ')
            if ch in 'nN':
                break

def DELETE_PASS():
    pass_ID=int(input('Enter Login ID: '))
    K=input('Deletion of account is permanant. Do you want to continue?[Y/N] ')
    if K in 'nN':
        return
    else:
        cs.execute(f'SELECT * FROM PASSENGERS where PID={pass_ID}')
        passenger=cs.fetchone()
        if not passenger:
            print('Invalid ID')
        else:
            cs.execute(f"DELETE FROM PASSENGERS where PID={pass_ID}")
            cs.execute(f"DELETE FROM BOOKINGS where PID={pass_ID}")
            db.commit()
            print('Passenger account and all related bookings deleted')


def SHOW_BOOK_PASS():
    pass_ID=int(input('Enter Login ID: '))
    cs.execute(f'SELECT * FROM PASSENGERS where PID="{pass_ID}"')
    passenger=cs.fetchone()
    if not passenger:
        print('Invalid ID')
    else:
        cs.execute(f"SELECT * FROM BOOKINGS where PID='{pass_ID}'")
        T=cs.fetchall()
        if not T:
            print('No booking made')
        else:
            print('Bookings from Login -',pass_ID)
            print('-----------------------------------------------------')
            print('Flight ID   Class      Adults  Children  Fare')
            print('-----------------------------------------------------')
            for i in T:
                if i[2]=='BUSINESS':
                    print(f"{i[1]}    {i[2]}     {i[3]}         {i[4]}      {i[5]}")
                else:
                    print(f"{i[1]}    {i[2]}      {i[3]}         {i[4]}      {i[5]}")
            print('-----------------------------------------------------')


def passenger_menu():
    while True:
        header("PASSENGER SERVICES")

        menu({
            "1": "Register Account",
            "2": "My Account",
            "3": "Delete Account",
            "4": "Booking Services",
            "Q": "Exit"
        })

        ch = input("Option: ").upper()

        if ch == '1':
            REGISTER_PASS()
        elif ch == '2':
            pid = SHOW_PASS()
            if pid:
                EDIT_PASS(pid)
        elif ch == '3':
            DELETE_PASS()
        elif ch == '4':
            from booking import booking_menu
            booking_menu()
        elif ch == 'Q':
            break
        else:
            print("Invalid option")
            pause()
