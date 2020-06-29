import time
import random
import pygame
from time import sleep
##\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##while True:
   ## pygame.mixer.init()
   ## pygame.mixer.music.load("Running_Free.mp3")
   ## pygame.mixer.music.play()
   ## print("                                                                                          PRESS START\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
   ## time.sleep(.5)
   ##print("\n\n\n")
   ## time.sleep(.5)
##pygame.mixer.music.fadeout(3000)
import os
import RPi.GPIO as GPIO
GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
pressed = ""
def start():
    pygame.mixer.init()
    pygame.mixer.music.load("Running_Free.mp3")
    pygame.mixer.music.play()
       ## print("                                                                                        PRESS START\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
       ## time.sleep(.5)
       ## print("\n\n\n")
       ## time.sleep(.5)
    while True:
        print("                                                                                        PRESS START\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(.5)
        print("\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(.5)
        if ( GPIO.input(17) == True ):
            GPIO.output(27, True)
            sleep(.5)
            GPIO.output(27, False)
            sleep(.5)
        if ( GPIO.input(17) == False ):
                break
    while True:
        if ( GPIO.input(17) == False ):
            GPIO.output(27, True)
            sleep(5)
            pressed = "Start"
            GPIO.output(27, False)
            sleep(.5)
            break
    return pressed
    pygame.mixer.music.fadeout(3000)
choice = ""
def buttons():
    while True:
        if ( GPIO.input(25) == False ):
                GPIO.output(13, True)
                choice = "Yes"
                GPIO.output(13, False)
                sleep(.5)
                break
        if ( GPIO.input(18) == False ):
                GPIO.output(5, True)
                choice = "No"
                GPIO.output(5, False)
                sleep(.5)
                break
    return choice
pressed = start()
pygame.mixer.init()
pygame.mixer.music.load("Spirit_Of_The_Wild.mp3")
pygame.mixer.music.play()
time.sleep(1.5)
print("                                                                                       ❧Would you like to go on a quest?")
time.sleep(.5)
print("                                                                                                     ❧Yes or No? ")
choice = buttons()
print(choice)
if choice == "Yes":
    time.sleep(1)
    print("                                                                           ❧Excellent! Prepare to embark on an adventure of a lifetime!")
while choice != "Yes":
    time.sleep(1)
    print("                                                                    ❧Then what are you doing here?! You are wasting precious time!")
    time.sleep(1)
    print("                                                                               ❧So are you going to be embarking or what?")
    time.sleep(1)
    print("                                                                                                  ❧Yes or No? ")
    choice = buttons()
    print(choice)
    if choice == "Yes":
        time.sleep(1)
        print("                                                                       ❧Excellent! Prepare to embark on an adventure of a lifetime!")
time.sleep(3)
print("")
print("")
print("                                                       ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘  _, ,  ,  _, _, ___,     _,  __,    ___,_   __,,_   ___, ,  ,,  , ___,_    ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘")
time.sleep(.04)
print("                                                       ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘ / \,|  | /_,(_,' |      / \,'|_,   ',| '|\ '|_,|_) ' |   |  ||\ |' | '|\   ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘")
time.sleep(.04)
print("                                                       ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘'\_X'\__|'\_  _)  |     '\_/  |     (_|  |-\ | '| \  _|_,'\__||'\| _|_,|-\  ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘")
time.sleep(.04)
print("                                                       ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘    `   `   `'    '      '    '          '  `'  '  `'        `'  `'    '  ` ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘")
time.sleep(.04)
print("                                                                          ⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦❦⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘")
time.sleep(.04)
print("")
print("")
time.sleep(0.5)
print("                                                                                                   A Interactive Story Game")
time.sleep(0.5)
print("                                                                                                           by Samantha")
print("")
print("")
time.sleep(1.5)
import Config
#Config.name = input("                                                                                     ❧What is your name? ")
print("                                                                                                  ❧Le Nathlam hí Adventurer!")
time.sleep(2)
print("                                                                                             ❧Le suilon to your Quest of Jafriunia!")
time.sleep(1.5)
roll = (random.randint(1,7))
print("                                                                                            ❧You were given a seven-sided dice to roll.")
time.sleep(1.5)
print("❧      ⚀")
time.sleep(1.5)
print("❧             ⚁")
time.sleep(1.5)
print("❧                     ⚂")
time.sleep(1.5)
print("❧                             ⚃")
time.sleep(1.5)
print("❧                                      ⚄")
time.sleep(1.5)
print("❧                                                ⚅")
time.sleep(1.5)
print("                                                                                                              ❧You rolled a " + str(roll) + ".")
time.sleep(1.5)
print("                                                                                            ❧According to your number you have been assigned the follwing role: ")
time.sleep(2.5)
if roll == 1:
    Config.role == "Paladin"
    print("                                                                                                ❧Le suilon Paladin. Your heroism is recongnized by all.")
    time.sleep(1.5)
    weapon = (random.randint(1,25))
    print("                                                                              ❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("                                                                                                  ❧The die has gifted the talent of dual weilding axes.")
        print("                                                                          ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                         ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                      ❧The die landed on " + str(grade) + ".")
            print("                                                                                                           ❧Your axes are rusted and dull.")
        elif grade <= 3:
            print("                                                                                                      ❧The die landed on " + str(grade) + ".")
            print("                                                                                    ❧Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("                                                                                                      ❧The die landed on " + str(grade) + ".")
            print("                                                                                      ❧Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                      ❧The die landed on " + str(grade) + ".")
            print("                                                                                      ❧Your axes are near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                      ❧The di landed on " + str(grade) + ".")
            print("                                                                                    ❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("                                                                                                  ❧The die has gifted you the talent of shield and sword weilding.")
        print("                                                                                ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                          ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                             ❧Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                          ❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                   ❧Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                     ❧Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                   ❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 15:
        print("                                                                                               ❧The die has gifted you the talent of two-handed sword weilding.")
        print("                                                                              ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                            ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                                            ❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                      ❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                        ❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                        ❧The die landed on " + str(grade) + ".")
            print("                                                                                        ❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 20:
        print("                                                                                                     ❧The die has gifted you the talent of spear weilding.")
        print("                                                                                  ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                            ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                                             ❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("                                                                                                       ❧The die has gifted you the talent of mace weilding.")
        print("                                                                                 ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                             ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                                              ❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                         ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("                                                                                                                          ❧Your invetory has...")
    ##This will where inventory will be added later. Planning on adding inventory as the game continues.
elif roll == 2:
    Config.role == "Illusionist"
    print("                                                                                                   ❧Le suilon Illusionist. Your slight of hand amazes the simple-minded.")
    time.sleep(1.5)
    weapon = (random.randint(1,25))
    print("                                                                                      ❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("                                                                                                         ❧The die has gifted the talent of scroll reading.")
        print("                                                                                  ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                            ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                     ❧Your scrolls are faded and burned on the edges.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                     ❧Your scrolls were made of decent parchment but are old and are in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                        ❧Your scolls are in decent condition, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your scrolls are near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                          ❧The di landed on " + str(grade) + ".")
            print("                                                                                         ❧Your scrolls are new from the Time. Hopefully they were made correctly.")
    elif weapon <= 10:
        print("                                                                                                 ❧The die has gifted you the talent of (fake) crystal orb reading.")
        print("                                                                               ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                             ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                 ❧Your orb has cracks in it and the crystal is clouded.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                    ❧Your orb was made of decent crystal with minor cracks but needs to be repaired.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                       ❧Your crystal orb is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                       ❧Your crystal orb is near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                        ❧Your crystal orb is new from the . Hopefully he made them correctly.")
    elif weapon <= 15:
        print("                                                                                                      ❧The die has gifted you the talent of tailsmen weilding.")
        print("                                                                                ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                               ❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                              ❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 20:
        print("                                                                                                      ❧The die has gifted you the talent of Staff weilding.")
        print("                                                                                ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                              ❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                             ❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("                                                                                                         ❧The die has gifted you the talent of wand weilding.")
        print("                                                                              ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                               ❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("                                                                                                                        ❧Your invetory has...")
    ##This is were items for inventory will go. Things will be added as story progresses.
elif roll == 3:
    Config.role == "Shadow"
    print("                                                                                               ❧Le suilon Shadow. Your alliance with the King lays deep within your being.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("                                                                                     ❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("                                                                                                      ❧The die has gifted the talent of dual weilding Karambits.")
        print("                                                                              ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                              ❧Your axes are rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                             ❧Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                             ❧Your axes are near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                          ❧The di landed on " + str(grade) + ".")
            print("                                                                                           ❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("                                                                                                 ❧The die has gifted you the talent of (small) Crossbow weilding.")
        print("                                                                                     ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                              ❧Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                      ❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                    ❧Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                   ❧Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                 ❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("                                                                                                      ❧The die has gifted you the talent of Bola weilding.")
        print("                                                                                   ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                              ❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                          ❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("                                                                                                     ❧The die has gifted you the talent of Chain Scythe weilding.")
        print("                                                                               ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                             ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                              ❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                         ❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("                                                                                                        ❧The die has gifted you the talent of Martial Arts.")
        print("                                                                               ❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("                                                                                                              ❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                                               ❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                       ❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                            ❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("                                                                                                          ❧The die landed on " + str(grade) + ".")
            print("                                                                                           ❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("                                                                                                                         ❧Your invetory has...")
    ##Inventory is going to be added later.
elif roll == 4:
    Config.role =="Priest"
    print("❧Le suilon Priest. The light of God guides you.")
    time.sleep(1.5)
    weapon = (random.randint(1,20))
    print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("❧The die has gifted the talent of Exorcisms.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are near mint condition. You have taken good care of them.")
        else:
            print("❧The di landed on " + str(grade) + ".")
            print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("❧The die has gifted you the talent of Thurible weilding.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("❧The die has gifted you the talent of Prayer.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("❧The die has gifted you the talent of Blessings.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("❧The die has gifted you the talent of Crucifix.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 5:
    Config.role == "Bard"
    print("❧Le suilon Bard. The music flows through you solmn.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("❧The die has gifted the talent of Lute.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are near mint condition. You have taken good care of them.")
        else:
            print("❧The di landed on " + str(grade) + ".")
            print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("❧The die has gifted you the talent of Ocarina.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("❧The die has gifted you the talent of Drums.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("❧The die has gifted you the talent of the Cittern.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("❧The die has gifted you the talent of Cli lyre.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 6:
    Config.role == "BeastMaster"
    print("❧Le suilon BeastMaster. The animals of Thoar Snia accept you as their own.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("❧The die has gifted the talent of dual weilding Tomahawks.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your axes are near mint condition. You have taken good care of them.")
        else:
            print("❧The di landed on " + str(grade) + ".")
            print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("❧The die has gifted you the talent of Zaghnal weilding.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("❧The die has gifted you the talent of Whip Sword weilding.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("❧The die has gifted you the talent of longsword weilding.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("❧The die has gifted you the talent of Club weilding.")
        print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
        print("❧Prepare to be bestowed a graded weapon.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is rusted and dull.")
        elif grade <= 3:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is near mint condition. You have taken good care of it.")
        else:
            print("❧The die landed on " + str(grade) + ".")
            print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
else:
    import Grave##add to grave the space configures to adjust to name length
    reroll = ("Would you like to reroll? ")
    print("❧You're DEAD! " + reroll)
    choice = buttons()
    if  choice == ("Yes"):
        import random
        reroll = (random.randint(7,10))
        if reroll == 7:
            Config.role = "Ghoul"
            print("❧You were resurrected as a Ghoul. Your talisman is a small strip of paper on your chest.")
            time.sleep(1.5)
            print("❧Your appearance indicates you have been recently deceased.")
            time.sleep(1.5)
            print("❧Anyone you come in contact with screams in terror and runs away.")
            import random
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 8:
            Config.role = "Trapper"
            print("❧Le suilon Trapper. Your trade is in tracking targets for money.")
            time.sleep(1.5)
            print("❧Your services have been requested by a neighboring kingdom for a service of secrecy.")
            time.sleep(1.5)
            print("❧You gleefully accept their terms.")
            import random
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 9:
            Config.role = "Vampire"
            print("❧You were saved by vampire blood, you are now a Vampire.")
            time.sleep(1.5)
            print("❧You are now the undead and can only travel at night.")
            time.sleep(1.5)
            print("❧But you are thirsty and must drink to stay alive.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        else:
            print("❧You fell down into the abyss.")
            time.sleep(1.5)
            print("❧Your soul was pulled to Hell by Satan himself.")
            time.sleep(1.5)
            print("❧That's unfortunate...")
            time.sleep(3.5)
            Start = ("❧Would you like to start over? ")
            print(Start)
            if choice == ("Yes"):
                Config.role = "Stranger"
                print("❧Le suilon Stranger. You lost your memory of your past.")
                time.sleep(1.5)
                print("❧Jafruinia has provided you a new life but you have to work for it.")
                time.sleep(1.5)
                print("❧Galu to you friend.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("❧The die has gifted the talent of dual weilding axes.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The di landed on " + str(grade) + ".")
                        print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("❧The die has gifted you the talent of shield and sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("❧The die has gifted you the talent of two-handed sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("❧The die has gifted you the talent of spear weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("❧The die has gifted you the talent of mace weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
            else:
                Config.role = "Ranger"
                print("❧Le suilon Ranger. Your weapon of choice is a Bow and Blade.")
                time.sleep(1.5)
                print("❧You are from an ancient line of decendants that used to protect the Royal court of Elves.")
                time.sleep(1.5)
                print("❧Your life's purpose is devoted to serving the one True King of Jafriunia.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("❧The die has gifted the talent of dual weilding axes.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The di landed on " + str(grade) + ".")
                        print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("❧The die has gifted you the talent of shield and sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("❧The die has gifted you the talent of two-handed sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("❧The die has gifted you the talent of spear weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("❧The die has gifted you the talent of mace weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
    else:
        print("❧Are you sure?")
        time.sleep(1.5)
        print("❧Well too bad, you are continuing anyway.")
        time.sleep(3)
        reroll = (random.randint(7,10))
        if reroll == 7:
            print("❧You were resurrected as a Ghoul. Your talisman is a small strip of paper on your chest.")
            time.sleep(1.5)
            print("❧Your appearance indicates you have been recently deceased.")
            time.sleep(1.5)
            print("❧Anyone you come in contact with screams in terror and runs away.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 8:
            print("❧Le suilon Trapper. Your trade is in tracking targets for money.")
            time.sleep(1.5)
            print("❧Your services have been requested by a neighboring kingdom for a service of secrecy.")
            time.sleep(1.5)
            print("❧You gleefully accept their terms.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 9:
            print("❧You were saved by vampire blood, you are now a Vampire.")
            time.sleep(1.5)
            print("❧You are now the undead and can only travel at night.")
            time.sleep(1.5)
            print("❧But you are thirsty and must drink to stay alive.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("❧The die has gifted the talent of dual weilding axes.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("❧The di landed on " + str(grade) + ".")
                    print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("❧The die has gifted you the talent of shield and sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("❧The die has gifted you the talent of two-handed sword weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("❧The die has gifted you the talent of spear weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("❧The die has gifted you the talent of mace weilding.")
                print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                print("❧Prepare to be bestowed a graded weapon.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is rusted and dull.")
                elif grade <= 3:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("❧The die landed on " + str(grade) + ".")
                    print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        else:
            print("❧You fell down into the abyss.")
            time.sleep(1.5)
            print("❧Your soul was pulled to Hell by Satan himself.")
            time.sleep(1.5)
            print("❧That's unfortunate...")
            time.sleep(3.5)
            Start = ("❧Would you like to start over? ")
            print(Start)
            if choice == ("Yes"):
                print("❧Le suilon Stranger. You lost your memory of your past.")
                time.sleep(1.5)
                print("❧Jafruinia has provided you a new life but you have to work for it.")
                time.sleep(1.5)
                print("❧Galu to you friend.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("❧The die has gifted the talent of dual weilding axes.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The di landed on " + str(grade) + ".")
                        print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("❧The die has gifted you the talent of shield and sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("❧The die has gifted you the talent of two-handed sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("❧The die has gifted you the talent of spear weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("❧The die has gifted you the talent of mace weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
            else:
                print("❧Le suilon Ranger. Your weapon of choice is a Bow and Blade.")
                time.sleep(1.5)
                print("❧You are from an ancient line of decendants that used to protect the Royal court of Elves.")
                time.sleep(1.5)
                print("❧Your life's purpose is devoted to serving the one True King of Jafriunia.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("❧The die has gifted the talent of dual weilding axes.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The di landed on " + str(grade) + ".")
                        print("❧Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("❧The die has gifted you the talent of shield and sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("❧The die has gifted you the talent of two-handed sword weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("❧The die has gifted you the talent of spear weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("❧The die has gifted you the talent of mace weilding.")
                    print("❧After you were gifted with your talent, the die transformed once more into a simple ten sided die.")
                    print("❧Prepare to be bestowed a graded weapon.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("❧The die landed on " + str(grade) + ".")
                        print("❧Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
time.sleep(3.5)
print("❧Would you like to continue? ")
choice = buttons()
if choice == "Yes":
    time.sleep(3)
    print("❧Gi nathlam hí in the Land of Jafriunia!")
while choice != "Yes":
    print("❧Prestad?! Would you like to continue? ")
    choice = buttons()
pygame.mixer.music.fadeout(3000)
time.sleep(3)
pygame.mixer.init()
pygame.mixer.music.load("Cup_Of_Mead.mp3")
pygame.mixer.music.play()
print("")
print("")
time.sleep(3)###Adding story to be read with eye
print("██████▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░")
time.sleep(.05)
print("██████████▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░                                                Wary from your travels, you step into a")
time.sleep(.05)
print("███████████████▓▓▒▒▒░░░░─░░░─░──░░░░░░░░                                                bustling run coun tavern . Upon entering,")
time.sleep(.05)
print("█████▓▒▒▒▓▓▓███▓██▓▓▒▒▒░░─░─────────────                                                the joyous noises ceased and glares directed")
time.sleep(.05)
print("███▓▒░░░░░▒▒▓█████████▓▒▒▒░░─────░──────                                                straight at the newcomer, you. The silence never")
time.sleep(.05)
print("███▒▒░░░░─░░░▒▓█████████▓▓▒▒▒░░─────────                                                broke as you soon move towards the bar. Eyes")
time.sleep(.05)
print("████▓▓▒▒░░░────░▒▓▓██████████▓▒▒▒░░░────                                                never leaving you as you did. The darkeep soon")
time.sleep(.05)
print("███████▓▓▓▒░░░─────░▒▒▓██████████▓▓▒░░░─                                                greeted you with a stoic expression which you")
time.sleep(.05)
print("████████████████▓▒▒░──░▒▒▒▓█████████▓▒░░                                                replied with your order of ale Unphased by")
time.sleep(.05)
print("█████████████████████▓▓▓▓▒░─░░▒▓▓▓▓▓▓▒▒░                                                the unfriendly looks, you simply start asking")
time.sleep(.05)
print("████████████████████████████▓▒░░░░░░░░──                                                about the history of the land. This was also")
time.sleep(.05)
print("███████████████████████████████▒────────                                                met with silence and glaces.")
time.sleep(.05)
print("██████████████▓▓▒▒███▓███████████▒──────                                                As your ale arrives, the backeep demanded your")
time.sleep(.05)
print("████████████▒░───░██▓▓█████▓███████░────                                                payment a little taken aback from the demand,")
time.sleep(.05)
print("████████████▒────░███▓█████▓██▓░▓███▒───                                                you wisely pay the keep and begin dunking")
time.sleep(.05)
print("█████████████░────▒██▓▓██▓███▓░──░███▓──                                                your ale. While you now minded your own")
time.sleep(.05)
print("██████████████─────▒████████▒─────▒████─                                                business, you didn't notice someone from at")
time.sleep(.05)
print("███████████████▒─────▓████▓──────▒▓████▒                                                across the roome eyeing you up and down.")
time.sleep(.05)
print("█████████████████▓▒──────────▒▓████████▓")
time.sleep(.05)
print("█████████████████████▓▓▓▓▓▓████████████▒")
time.sleep(.05)
print("█████████▓▓▓▒▓▓▓███████████████████████▒")
time.sleep(.05)
print("███▓████▓▒░─────░░███████████▓▓▓▓▓▓▒░░░─")
time.sleep(.05)
print("██▓▓███▒░░─────────▓████████▒░░▒▒▒░░░───")
time.sleep(.05)
print("██▓███▓░░───────────███████▓░░░░░░░─────")
time.sleep(.05)
print("██▓███░────────░────▓██████▒────────────")
time.sleep(.05)
print("█▓▓██▓─────────▓────▓█████▓░────────────")
time.sleep(.05)
print("█▓▓██░─────────█▒───▓█████▒─────────────")
time.sleep(.05)
print("█▓▓██──────────█▒───▓█████░─────────────")
time.sleep(.05)
print("█▓▓██─────────░█────▒█████──────────────")
time.sleep(.05)
print("█▓▒██─────────█░────░████▓──────────────")
time.sleep(.05)
print("█▓░▓█▓──────░█▒──────████▒──────────────")
time.sleep(.05)
print("█▓░░███░─░▒▓█▒───────████▒──────────────")
time.sleep(.05)
print("██▒─░██████▓─────────████░──────────────")
time.sleep(.05)
print("██▓░─────────────────▓███░──────────────")
time.sleep(.05)
print("██▓▒─────────────────▒███░──────────────")
time.sleep(.05)
print("██▓▒░────────────────░███───────────────")
time.sleep(.05)
print("███▓░─────────────────███───────────────")
time.sleep(.05)
print("███▓░░────────────────██▓───────────────")
time.sleep(.05)
print("████▒░────────────────▓█▓───────────────")
time.sleep(.05)
print("████▓░────────────────▓█▒───────────────")
time.sleep(.05)
print("█████▒────────────────▒█▒───────────────")
time.sleep(.05)
print("█████▒────────────────▒█▒───────────────")
time.sleep(.05)
print("██████░───────────────▒█▒───────────────")
time.sleep(.05)
print("██████▒───────────────▒█░───────────────")
time.sleep(.05)
print("██████▓░──────────────░▓░───────────────")
time.sleep(.05)
print("███████▒──────────────░▓▒───────────────")
time.sleep(.05)
print("████████░──────────────▓▒───────────────")
time.sleep(.05)
print("████████▓░─────────────▒▒───────────────")
time.sleep(.05)
print("█████████▒─────────────▒▒───────────────")
time.sleep(.05)
print("██████████▒────────────▒░───────────────")
time.sleep(.05)
print("███████████▒───────────▒░───────────────")
time.sleep(.05)
print("███████████▓▒──────────░░───────────────")
time.sleep(.05)
print("█████████████▒─────────░░───────────────")
time.sleep(.05)
print("█████████████▓▒░────────────────────────")
time.sleep(15)##This will be running as a 30 second time sleep when playing
pygame.mixer.music.fadeout(3000)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(3)
###if Config.role == "Paladin":
###    print(Config.role)
###    print(Config.weapon)
print("                                                                                                               CREDITS")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                Created by.................................................................Samantha Weaver")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                                                                 SONGS")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                Introduction....................................................'Running Free' by Peter Crowley")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                 Background...................................................'Spirit Of The Wild by Burnuhville")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                Tarvern.........................................................'Cup Of Mead' by Mark Streitenfeld")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                                              THANK YOU!")
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("")
time.sleep(.3)
print("                                                                                               THE END")
