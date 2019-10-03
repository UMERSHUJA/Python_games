
# build games using while loop
# build a guessing game ...
# guess a particular number using while loop in just 3 tries...
print('''
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


''')




print('''
Guess any number from 0 to 9,
you have only three chances to guess that number
''')
import random
secret = random.randint(0, 9)
i = 1
while i<=3:
    temp = int(input('Guess: '))
    if temp == secret:
        print('you win!')
        break
    i += 1
else:
    print("Sorry! you failed")


