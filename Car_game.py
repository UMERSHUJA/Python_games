
# build car game using while loop


print('''
                                  Car Game
Created by: 
 ____  _   _ ___ ____  ____    _    _   _ 
/ ___|| | | |_ _|  _ \/ ___|  / \  | | | |
\___ \| | | || || |_) \___ \ / _ \ | |_| |
 ___) | |_| || ||  _ < ___) / ___ \|  _  |
|____/ \___/|___|_| \_\____/_/   \_\_| |_|
                                          
 __  __ _   _ _   _    _    __  __ __  __    _    ____  
|  \/  | | | | | | |  / \  |  \/  |  \/  |  / \  |  _ \ 
| |\/| | | | | |_| | / _ \ | |\/| | |\/| | / _ \ | | | |
| |  | | |_| |  _  |/ ___ \| |  | | |  | |/ ___ \| |_| |
|_|  |_|\___/|_| |_/_/   \_\_|  |_|_|  |_/_/   \_\____/ 


Type help first, before running the game

''')

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if started:              
            print("Car is already started!")
        else:
            started = True
            print("Car started!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started=False
            print("Car stopped!")

    elif command == "quit":
        break

    else:
        print("I don't understand that...")


