from admin import admin_menu
from passenger import passenger_menu
from ui import header, menu, pause


ADMIN_ID = "admin"
ADMIN_PWD = "abc123"

while True:
    header("AIRWAYS RESERVATION SYSTEM")

    menu({
        "A": "Admin Login",
        "S": "Service Login",
        "Q": "Exit"
    })

    ch = input("Select option: ").upper()

    if ch == 'A':
        uid = input("Admin ID: ")
        pwd = input("Password: ")

        if uid == ADMIN_ID and pwd == ADMIN_PWD:
            admin_menu()
        else:
            print("Invalid credentials")
            pause()

    elif ch == 'S':
        passenger_menu()

    elif ch == 'Q':
        print("Thank you for using Airways Reservation System")
        break

    else:
        print("Invalid option")
        pause()
