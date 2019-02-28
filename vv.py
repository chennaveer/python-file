import random

while true:
    d = input("press r to roll,q to quit: ")
    if d == 'r':
        print("you got:",random.randomint(1,6))

     elif d == 'q':
         print("bye!")
         exit() 


print("end")