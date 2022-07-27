##########################################################################################################################################################
## Student Starting Template Below ##

import random
## Planet Statistics ##
## Radius in km
planet1 = "Saturn"
planet1Radius = 58232
planet1Position = 6
planet1RingNumber = 7

planet2 = "Uranus"
planet2Radius = 25362
planet2Position = 7
planet2RingNumber = 13

planet3 = "Neptune"
planet3Radius = 24622
planet3Position = 8
planet3RingNumber = 5

score = 0

## Students should code question 1 themselves ()

##print("Which planet has a radius of " + str(planet1Radius) + " km?")
##print(planet1 + "\n" + planet2 + "\n" + planet3)
##answer1 = planet1
##userResponse1 = input("Enter " + planet1 + ", " + planet2 + ", or " + planet3 + ": ")
##if userResponse1 == answer1:
##    print("Correct!")
##    print(answer1 + " has a radius of " + str(planet1Radius) + " km")
##    score = score + 1
##else:
##    print("Incorrect!")

## Students can use the following code as templates for questions 2 and 3
## Focus on determining the answer via code for Q2
userResponse2 = input("Enter " + planet1 + ", " + planet2 + ", or " + planet3 + ": ")
if userResponse2 == answer2:
    print("Correct!")
    print(answer2 + " has the most rings")
    score = score + 1
else:
    print("Incorrect!")
print()

## Focus on determining the question and answer based on the random number for Q3
userResponse3 = input("Enter " + planet1 + ", " + planet2 + ", or " + planet3 + ": ")
if userResponse3 == answer3:
    print("Correct!")
    print(answer3 + " is " + str(randomPosition) + " planets from the Sun")
    score = score + 1
else:
    print("Incorrect!")
print()
