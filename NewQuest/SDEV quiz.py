##A program that counts from 0 to 100 in incraments of 5
import time
count = 0
number = input("Would you like to count in fives? ").lower()
time.sleep(1)
## Counting by fives
if number == "no":
    time.sleep(1)
    print("I made this program for you! You will count by fives!")
    while count <= 100 :
        time.sleep(1)
        print(str(count) + " Bye bye bye.")
        count = count + 5
elif number == "yes":
    while count <= 100 :
        time.sleep(1)
        print(str(count) + " Bye bye bye.")
        count = count + 5    
time.sleep(1)    
print("There! See how easy that was!")
