import time
import random
reroll = (random.randint(7,10))
if reroll == 7:
    print("You were resurrected as a Ghoul. Your talisman is a small strip of paper on your chest.")
    time.sleep(1.5)
    print("Your appearance indicates you have been recently deceased.")
    time.sleep(1.5)
    print("Anyone you come in contact with screams in terror and runs away.")
elif reroll == 8:
    print("Le suilon Trapper. Your trade is in tracking targets for money.")
    time.sleep(1.5)
    print("Your services have been requested by a neighboring kingdom for a service of secrecy.")
    time.sleep(1.5)
    print("You gleefully accept their terms.")
elif reroll == 9:
    print("You were saved by vampire blood, you are now a Vampire.")
    time.sleep(1.5)
    print("You are now the undead and can only travel at night.")
    time.sleep(1.5)
    print("But you are thirsty and must drink to stay alive.")
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
        print("Thoar Snia has provided you a new life but you have to work for it.")
        time.sleep(1.5)
        print("Galu to you friend.")
    else:
        print("Le suilon Ranger. Your weapon of choice is a Bow and Blade.")
        time.sleep(1.5)
        print("You are from an ancient line of decendants that used to protect the Royal court of Elves.")
        time.sleep(1.5)
        print("Your life's purpose is devoted to serving the one True King of Thoar Snia.")
