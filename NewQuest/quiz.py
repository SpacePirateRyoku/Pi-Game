##5 question quiz
##made by Samantha Weaver
##Version 69.69 hehe
##question 1
import time
print("The Pointless Quiz")
##created 10/08/19
##revised 10/09/19
time.sleep(.5)
##Tracks points
points = 0
print("Finish this lyric: 'Ground control to...'")
time.sleep(.5)
print("A. Moonbase")
time.sleep(.5)
print("B. Major Tom")
time.sleep(.5)
print("C. Tower")
time.sleep(.5)
print("D. 747")
time.sleep(.5)
##Answer
ques_1 = input("What is your answer?\n").lower()
time.sleep(.5)
if ques_1 == "a":
    print("Incorrect.")
    time.sleep(.5)
    print("Very close. Keep reaching for the stars.")
elif ques_1 == "b":
    print("Correct!")
    time.sleep(.5)
    print("Good job! You know David Bowie!")
    ##adding points to correct answer
    points +=1
elif ques_1 == "c":
    print("Incorrect.")
    time.sleep(.5)
    print("Nice try, but we are not talking planes.")
elif ques_1 == "d":
    print("Incorrect.")
    time.sleep(.5)
    print("That's a plane!")
else:
    time.sleep(.5)
    print("That isn't an answer. Minus 50 points from Griffondor!")
##question 2
print("")
time.sleep(1.5)
print("The answer is really big.")
time.sleep(.5)
print("A. THE ANSWER.")
time.sleep(.5)
print("B. Really big.")
time.sleep(.5)
print("C. An elephant.")
time.sleep(.5)
print("D. The data given is insufficient.")
time.sleep(.5)
##Answer
ques_2 = input("What is your answer?\n").lower()
time.sleep(.5)
if ques_2 == "a":
    print("Correct!")
    time.sleep(.5)
    print("Good job. You are smart!")
    ##adding points to correct answer
    points +=1
elif ques_2 == "b":
    print("Incorrect.")
    time.sleep(.5)
    print("Hey now, get out of the gutter.")
elif ques_2 == "c":
    print("Incorrect.")
    time.sleep(.5)
    print("Nice try, but we aren't talking about big animals.")
elif ques_2 == "d":
    print("Incorrect.")
    time.sleep(.5)
    print("What are you...a computer?")
else:
    time.sleep(.5)
    print("That isn't an answer. Minus 50 points from Slytheren!")
##question 3
print("")
time.sleep(1.5)
print("Is the glass...?")
time.sleep(.5)
print("A. Half Full?")
time.sleep(.5)
print("B. Half empty?")
time.sleep(.5)
print("C. Doesn't have enough ice?")
time.sleep(.5)
print("D. Not a glass at all.")
time.sleep(.5)
##Answer
ques_3 = input("What is your answer?\n").lower()
if ques_3 == "a":
    print("Of course you are an optimist.")
    ##adding points to correct answer
    points += 1
elif ques_3 == "b":
    print("Of course you are a pessimist.")
    ##adding points to correct answer
    points += 1
elif ques_3 == "c":
    print("You sound like an Alchoholic...")
    ##adding points to correct answer
    points += 1
elif ques_3 == "d":
    print("I think I should run away.")
    ##adding points to correct answer
    points += 1
else:
    print("That isn't an answer! Minus 50 points from Hufflepuff!")
    ##adding points to correct answer
    points += 1
##question 4
print("")
time.sleep(1.5)
print("What's my name? What's my name?")
time.sleep(.5)
print("A. Sam")
time.sleep(.5)
print("B. Michael")
time.sleep(.5)
print("C. Courtney")
time.sleep(.5)
print("D. Uma")
time.sleep(.5)
##Answer
ques_4 = input("What is you answer?\n").lower()
if ques_4 == "a":
    print("Incorrect.")
    time.sleep(.5)
    print("Yes that is my name, but not the answer I was looking for.")
elif ques_4 == "b":
    print("Incorrect.")
    time.sleep(.5)
    print("That's nice and all, but we aren't here to talk about you Michael.")
elif ques_4 == "c":
    print("Incorrect.")
    time.sleep(.5)
    print("Who dat?")
elif ques_4 == "d":
    print("Correct!")
    time.sleep(.5)
    print("SAY IT LOUDER!")
    ##adding points to correct answer
    points += 1
else:
    time.sleep(.5)
    print("That isn't an answer! Minus 50 points from Ravenclaw!")
##question 5
print("")
time.sleep(1.5)
print("On Sunday in Florida it is illegal for a single woman to do what?")
time.sleep(.5)
print("A. Smoke")
time.sleep(.5)
print("B. Wear heels")
time.sleep(.5)
print("C. Skydive")
time.sleep(.5)
print("D. Drive without a man in the passenger seat")
time.sleep(.5)
##Answer
ques_5 = input("What is your answer?\n").lower()
if ques_5 == "a":
    print("Incorrect.")
    time.sleep(.5)
    print("She gets to have that smoke!")
elif ques_5 == "b":
    print("Incorrect.")
    time.sleep(.5)
    print("Girl gotta look good.")
elif ques_5 == "c":
    print("Correct!")
    time.sleep(.5)
    print("Like what the hell?")
    ##adding points to correct answer
    points += 1
elif ques_5 == "d":
    print("Incorrect.")
    time.sleep(.5)
    print("Why would you guess this?!")
else:
    time.sleep(.5)
    print("This isn't an answer. You have been denied entrance into Hogwarts. You are not a wizard Harry.")
##Conclusion
print("")
time.sleep(1.5)
print("Congratulations! You have finished the quiz!")
time.sleep(.5)
#Adding up points for final score
if points == 5:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("You got a perfect score. You deserve a lollipop...but I don't have one. So...sorry?")
elif points == 4:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("So close but no cigar. Though cigars smell good.")
elif points == 3:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("You missed some there. That's alright this quiz is pointless anyway.")
elif points == 2:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("Well, that's a good number. Though that's some weak sauce right there.")
elif points == 1:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("It was the glass question, wasn't it?")
else:
    print("You got " + str(points) + ".")
    time.sleep(.5)
    print("You didn't even try...you suck.")
