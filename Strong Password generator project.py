# Strong Password generator 

import random

Alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
Numbers=list(range(10))
Symbols=list("!@#$%^&*()_+)")

Alphabet_Length=int(input("How many Alphabets would you like to have in your password: "))
Number_Length=int(input("How many Numbers would you like to have in your password: " ))
Special_Symbols=int(input("How many Special_Symbols would you like to have in your password: "))

Password=[]
for i in range(Alphabet_Length):
    Password.append(random.choice(Alphabets))

for i in range(Number_Length):
    Password.append(str(random.choice(Numbers)))

for i in range(Special_Symbols):
    Password.append(random.choice(Symbols))

random.shuffle(Password)

Final_Password=" "
for i in Password:
    Final_Password=Final_Password + i
print(Final_Password)











