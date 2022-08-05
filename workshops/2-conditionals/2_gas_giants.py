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

## Question 1 Below ##
## Q1: Which planet has a radius of (planet1Radius) km?



## Question 2 Here ##
## Q2: Which of the following planets have the most rings?
## Focus on determining the answer via code for Q2, use the provided code for inputting and grading the user answer
userResponse2 = input("Enter " + planet1 + ", " + planet2 + ", or " + planet3 + ": ")
if userResponse2 == answer2:
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print(answer2 + " has the most rings")
print()



## Question 3 Here ##
## Q3: Which planet is (random planet position out of the 3 variable positions) planets away from the Sun?
## Focus on determining the question and answer based on the random number for Q3, use the provided code for inputting and grading the user answer
userResponse3 = input("Enter " + planet1 + ", " + planet2 + ", or " + planet3 + ": ")
if userResponse3 == answer3:
    print("Correct!")
    print(answer3 + " is " + str(randomPosition) + " planets from the Sun")
    score = score + 1
else:
    print("Incorrect!")
print()




## Print Final Score ## 
