import time
from playsound import playsound
playsound("C:\\Users\\samaw\\AppData\\Local\\Programs\\Python\\Python37-32\\New Quest\\battle.mp3")
time.sleep(1.5)
Play = input("                                                                       ❧Would you like to go on a quest?")
print("                                                                                       ❧Yay or Nay? ").lower()
if Play == "yay":
    time.sleep(1)
    print("                                                                     ❧Excellent! Prepare to embark on an adventure of a lifetime!")
while Play != "yay":
    time.sleep(1)
    print("                                                                 ❧Then what are you doing here?! You are wasting precious time!")
    time.sleep(1)
    print("                                                                              ❧So are you going to be embarking or what?")
    time.sleep(1)
    Play = input("                                                                                     ❧Yay or Nay?\n").lower()
time.sleep(3)
import title
time.sleep(3)
import Config
Config.name = input("❧What is your name? ")
print("❧Le Nathlam hi " + Config.name + "~!")
time.sleep(2)
print("❧Le suilon to your Quest of Jafruinia!")
time.sleep(1.5)
import Rolling
time.sleep(3.5)
Continue = input("❧Would you like to continue? ")
if Continue.upper() == "YES":
    time.sleep(3)
    print("❧Gi nathlam hí in the Land of Jafruinia!")###look into something different
while Continue.upper() != "YES":
    Continue = input("❧Prestad?! Would you like to continue? ")
time.sleep(3)
import Face
time.sleep(30)
print("")
print("")
print("")
print("")

