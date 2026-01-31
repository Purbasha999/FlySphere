from database import db, cs
from ui import header, menu, pause

def SEARCH():
    while True:
        print('ONE-WAY FLIGHT:')        
        From=input('From:- ')
        To=input('To:- ')
        sql=f"Select * from AIRLINES where DLocation='{From}' and ALocation= '{To}' order by Date"
        cs.execute(sql)
        T=cs.fetchall()
        if T:
            print( '----------------------------------------------------------')
            print('Flight ID   Date         Departure   Arrival    Basic Fare')
            print( '----------------------------------------------------------')
            for i in T:
                print(f"{i[0]}    {i[1]}   {i[4]}    {i[5]}   {i[6]}")
            print( '----------------------------------------------------------')
            print()
        else:
            print('Sorry. No flights found')
        K=input('Continue searching? [Y/N]: ')
        if K in 'nN':
            break
def BOOK():
    print('NOTE:- 1.Children(below 12 years of age) will get 10% discount.')
    print('       2.Fare for Premium = 2 times Economy')
    print('       3.Fare for Business = 5 times Economy')
    ID=int(input('Enter Login ID: '))
    cs.execute(f"SELECT * FROM PASSENGERS WHERE PID={ID}")
    pass_check=cs.fetchone()
    if not pass_check:
        print('Invalid ID. Booking Failed.')
    else:
        flight=input('Enter Flight ID: ').upper()
        cs.execute(f'SELECT * FROM AIRLINES WHERE AID="{flight}"')
        air_check=cs.fetchone()
        if not air_check:
            print('Invalid Flight ID. Booking Failed.')
        else:            
            cs.execute(f"SELECT * from BOOKINGS where PID={ID} and AID= '{flight}'")
            book_check=cs.fetchone()
            if not book_check:
                In_Fare=air_check[6]                
                adult=int(input('No. of adults: '))
                child=int(input('No. of children: '))
                air_class=input('Economy/Premium/Business class?[E/P/B]: ') .upper()
                if air_class=='B':
                    Class='BUSINESS'
                elif air_class=='P':
                    Class='PREMIUM'
                else:
                    Class='ECONOMY'
                if Class=='BUSINESS':
                    In_Fare*=5
                elif Class=='PREMIUM':
                    In_Fare*=2
                Total=In_Fare*(adult+(child*0.9))
                sql=f'INSERT INTO BOOKINGS values ({ID},"{flight}","{Class}", {adult},{child},{Total})'
                cs.execute(sql)
                db.commit()            
                print('Your Fare is Rs.', Total)
                print("Booking successful")
            else:
                print("Already booked from this account")

            
def CANCEL_BOOK():
    print('NOTE:- Cancellation charge is 50% of total fare')
    ID=int(input('Enter Login ID: '))
    flight=input('Enter flight ID: ')
    K=input('Deletion of booking is permanant. Do you want to continue?[Y/N] ')
    if K in 'nN':
        return
    else:
        cs.execute(f"SELECT * FROM PASSENGERS WHERE PID={ID}")
        pass_check=cs.fetchone()
        if not pass_check:
            print('Invalid ID.')
        else:
            cs.execute(f'SELECT * FROM AIRLINES WHERE AID="{flight}"')
            air_check=cs.fetchone()
            if not air_check:
                print('Invalid Flight ID.')
            else:
                cs.execute(f"SELECT * FROM BOOKINGS WHERE PID={ID} and AID= '{flight}'")
                book_check=cs.fetchone()
                if not book_check:
                    print('No such booking made.')
                else:
                    refund=book_check[5]
                    sql=f"DELETE from BOOKINGS where AID='{flight}' and PID= {ID}"
                    cs.execute(sql)
                    print('Booking Cancelled')
                    print('Rs.',refund/2,'will be refunded.')
                    db.commit()

def booking_menu():
    while True:
        header("BOOKING MENU")

        menu({
            "1": "Search Flights",
            "2": "Book Flight",
            "3": "Cancel Booking",
            "4": "Booking History",
            "Q": "Back"
        })

        ch = input("Option: ").upper()

        if ch == '1':
            SEARCH()
        elif ch == '2':
            BOOK()
        elif ch == '3':
            CANCEL_BOOK()
        elif ch == '4':
            from passenger import SHOW_BOOK_PASS
            SHOW_BOOK_PASS()
        elif ch == 'Q':
            break
        else:
            print("Invalid option")
            pause()
