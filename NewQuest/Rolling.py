import time
import Config
print("❧You were given a seven-sided dice to roll.")
import random
roll = (random.randint(7,7))
time.sleep(1.5)
print("❧ ⚀")
time.sleep(1.5)
print("❧       ⚁")
time.sleep(1.5)
print("❧             ⚂")
time.sleep(1.5)
print("❧                   ⚃")
time.sleep(1.5)
print("❧                          ⚄")
time.sleep(1.5)
print("❧                                 ⚅")
time.sleep(1.5)
print("❧You rolled a " + str(roll) + ".")
time.sleep(1.5)
print("❧According to your number you have been assigned the follwing role: ")
time.sleep(2.5)
if roll == 1:
    Config.role == "Paladin"
    print("❧Le suilon Paladin. Your heroism is recongnized by all.")
    time.sleep(1.5)
    weapon = (random.randint(1,20))
    print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 2:
    Config.role == "Illusionist"
    print("Le suilon Illusionist. Your slight of hand amazes the simple-minded.")
    time.sleep(1.5)
    weapon = (random.randint(1,20))
    print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 3:
    Config.role == "Shadow"
    print("Le suilon Shadow. Your alliance with the King lays deep within your being.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    weapon = (random.randint(1,20))
    print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 4:
    Config.role =="Priest"
    print("Le suilon Priest. The light of God guides you.")
    time.sleep(1.5)
    weapon = (random.randint(1,20))
    print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 5:
    Config.role == "Bard"
    print("Le suilon Bard. The music flows through you solmn.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
elif roll == 6:
    Config.role == "BeastMaster"
    print("Le suilon BeastMaster. The animals of Thoar Snia accept you as their own.")
    time.sleep(1.5)
    weapon = (random.randint (1,20))
    print("❧Your seven sided di magically turned into a twenty sided di, you roll it out of curiosity...")
    time.sleep(1.5)
    if weapon <= 5:
        print("The die has gifted the talent of dual weilding axes.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your axes were made of decent metal but are old and are in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your axes are near mint condition. You have taken good care of them.")
        else:
            print("The di landed on " + str(grade) + ".")
            print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 5:
        print("The die has gifted you the talent of shield and sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your shield has chunks taken from it and your sword is dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are near mint condition. You have taken good care of them.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
    elif weapon <= 10:
        print("The die has gifted you the talent of two-handed sword weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
    elif weapon <= 15:
        print("The die has gifted you the talent of spear weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
    else:
        print("The die has gifted you the talent of mace weilding.")
        grade = (random.randint(1,10))
        if grade == 1:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is rusted and dull.")
        elif grade <= 3:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is made of decent metal but is old and is in need of repair.")
        elif grade <= 6:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is in good standing, you don't need repairs for a while.")
        elif grade <= 8:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is near mint condition. You have taken good care of it.")
        else:
            print("The die landed on " + str(grade) + ".")
            print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
    print("❧Your invetory has...")
else:
    import Grave##add to grave the space configures to adjust to name length
    reroll = ("Would you like to reroll? ")
    Var_Eq = input("You're DEAD! " + reroll).lower()
    if  Var_Eq == ("yes"):
        import random
        reroll = (random.randint(7,10))
        if reroll == 7:
            Config.role = "Ghoul"
            print("You were resurrected as a Ghoul. Your talisman is a small strip of paper on your chest.")
            time.sleep(1.5)
            print("Your appearance indicates you have been recently deceased.")
            time.sleep(1.5)
            print("Anyone you come in contact with screams in terror and runs away.")
            import random
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 8:
            Config.role = "Trapper"
            print("Le suilon Trapper. Your trade is in tracking targets for money.")
            time.sleep(1.5)
            print("Your services have been requested by a neighboring kingdom for a service of secrecy.")
            time.sleep(1.5)
            print("You gleefully accept their terms.")
            import random
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 9:
            Config.role = "Vampire"
            print("You were saved by vampire blood, you are now a Vampire.")
            time.sleep(1.5)
            print("You are now the undead and can only travel at night.")
            time.sleep(1.5)
            print("But you are thirsty and must drink to stay alive.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        else:
            print("You fell down into the abyss.")
            time.sleep(1.5)
            print("Your soul was pulled to Hell by Satan himself.")
            time.sleep(1.5)
            print("That's unfortunate...")
            time.sleep(3.5)
            Start = ("Would you like to start over? ")
            unfortunate = input(Start)
            if unfortunate.upper() == ("YES"):
                Config.role = "Stranger"
                print("Le suilon Stranger. You lost your memory of your past.")
                time.sleep(1.5)
                print("Jafruinia has provided you a new life but you have to work for it.")
                time.sleep(1.5)
                print("Galu to you friend.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("The die has gifted the talent of dual weilding axes.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("The di landed on " + str(grade) + ".")
                        print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("The die has gifted you the talent of shield and sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("The die has gifted you the talent of two-handed sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("The die has gifted you the talent of spear weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("The die has gifted you the talent of mace weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
            else:
                Config.role = "Ranger"
                print("Le suilon Ranger. Your weapon of choice is a Bow and Blade.")
                time.sleep(1.5)
                print("You are from an ancient line of decendants that used to protect the Royal court of Elves.")
                time.sleep(1.5)
                print("Your life's purpose is devoted to serving the one True King of Jafriunia.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("The die has gifted the talent of dual weilding axes.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("The di landed on " + str(grade) + ".")
                        print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("The die has gifted you the talent of shield and sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("The die has gifted you the talent of two-handed sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("The die has gifted you the talent of spear weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("The die has gifted you the talent of mace weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
    else:
        print("Are you sure?")
        time.sleep(1.5)
        print("Well too bad, you are continuing anyway.")
        time.sleep(3)
        reroll = (random.randint(7,10))
        if reroll == 7:
            print("You were resurrected as a Ghoul. Your talisman is a small strip of paper on your chest.")
            time.sleep(1.5)
            print("Your appearance indicates you have been recently deceased.")
            time.sleep(1.5)
            print("Anyone you come in contact with screams in terror and runs away.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 8:
            print("Le suilon Trapper. Your trade is in tracking targets for money.")
            time.sleep(1.5)
            print("Your services have been requested by a neighboring kingdom for a service of secrecy.")
            time.sleep(1.5)
            print("You gleefully accept their terms.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        elif reroll == 9:
            print("You were saved by vampire blood, you are now a Vampire.")
            time.sleep(1.5)
            print("You are now the undead and can only travel at night.")
            time.sleep(1.5)
            print("But you are thirsty and must drink to stay alive.")
            weapon = (random.randint(1,20))
            print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
            time.sleep(1.5)
            if weapon <= 5:
                print("The die has gifted the talent of dual weilding axes.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes were made of decent metal but are old and are in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your axes are near mint condition. You have taken good care of them.")
                else:
                    print("The di landed on " + str(grade) + ".")
                    print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 5:
                print("The die has gifted you the talent of shield and sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your shield has chunks taken from it and your sword is dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are near mint condition. You have taken good care of them.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
            elif weapon <= 10:
                print("The die has gifted you the talent of two-handed sword weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
            elif weapon <= 15:
                print("The die has gifted you the talent of spear weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
            else:
                print("The die has gifted you the talent of mace weilding.")
                grade = (random.randint(1,10))
                if grade == 1:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is rusted and dull.")
                elif grade <= 3:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is made of decent metal but is old and is in need of repair.")
                elif grade <= 6:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is in good standing, you don't need repairs for a while.")
                elif grade <= 8:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is near mint condition. You have taken good care of it.")
                else:
                    print("The die landed on " + str(grade) + ".")
                    print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
            print("❧Your invetory has...")
        else:
            print("You fell down into the abyss.")
            time.sleep(1.5)
            print("Your soul was pulled to Hell by Satan himself.")
            time.sleep(1.5)
            print("That's unfortunate...")
            time.sleep(3.5)
            Start = ("Would you like to start over? ")
            unfortunate = input(Start)
            if unfortunate.upper() == ("YES"):
                print("Le suilon Stranger. You lost your memory of your past.")
                time.sleep(1.5)
                print("Jafruinia has provided you a new life but you have to work for it.")
                time.sleep(1.5)
                print("Galu to you friend.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("The die has gifted the talent of dual weilding axes.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("The di landed on " + str(grade) + ".")
                        print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("The die has gifted you the talent of shield and sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("The die has gifted you the talent of two-handed sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("The die has gifted you the talent of spear weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("The die has gifted you the talent of mace weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
            else:
                print("Le suilon Ranger. Your weapon of choice is a Bow and Blade.")
                time.sleep(1.5)
                print("You are from an ancient line of decendants that used to protect the Royal court of Elves.")
                time.sleep(1.5)
                print("Your life's purpose is devoted to serving the one True King of Jafriunia.")
                weapon = (random.randint(1,20))
                print("❧Your seven sided die magically turned into a twenty sided die, you roll it out of curiosity...")
                time.sleep(1.5)
                if weapon <= 5:
                    print("The die has gifted the talent of dual weilding axes.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes were made of decent metal but are old and are in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your axes are near mint condition. You have taken good care of them.")
                    else:
                        print("The di landed on " + str(grade) + ".")
                        print("Your axes are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 5:
                    print("The die has gifted you the talent of shield and sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your shield has chunks taken from it and your sword is dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword was made of decent metal and your shield is trimmed in a decent reforcement metal\nbut need to be repaired.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are near mint condition. You have taken good care of them.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword and shield are new from the blacksmith. Hopefully he made them correctly.")
                elif weapon <= 10:
                    print("The die has gifted you the talent of two-handed sword weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your sword is new from the blacksmith. Hopefully he made it correctly.")
                elif weapon <= 15:
                    print("The die has gifted you the talent of spear weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your spear is new from the blacksmith. Hopefully he made it correctly.")
                else:
                    print("The die has gifted you the talent of mace weilding.")
                    grade = (random.randint(1,10))
                    if grade == 1:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is rusted and dull.")
                    elif grade <= 3:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is made of decent metal but is old and is in need of repair.")
                    elif grade <= 6:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is in good standing, you don't need repairs for a while.")
                    elif grade <= 8:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is near mint condition. You have taken good care of it.")
                    else:
                        print("The die landed on " + str(grade) + ".")
                        print("Your mace is new from the blacksmith. Hopefully he made it correctly.")
                print("❧Your invetory has...")
