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

# print(Password)
Final_Password=" "
for i in Password:
    Final_Password=Final_Password + i
print(Final_Password)


# .Find and remove a specific element from the list 
# List=[1,2,3,4,5,6]
# print(List[2])

# List=[1,2,3,4,5,6]
# List.remove(4)
# print(List)


# find and update the specific element in the string list


# Find max and min in the list using one loop


# find average of the list

# Num=(1,2,3,4,5,6,7,8)
# Average=0
# for i in Num:
#     Average=Average + i
# Average= Average / 8    
# print(Average)




def Total():
    Num1=5
    Num2=10
    sum=Num1+Num2
    print(sum)

Total()    










