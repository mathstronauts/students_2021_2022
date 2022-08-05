## Basic function
def testFunction1():
    print("You called testFunction1!")

## Function with string input
def testFunction2(word):
    print("The string you entered is: " + word)

## Function with integer or float input
def testFunction3(number):
    inputTimesTwo = number * 2
    print(inputTimesTwo)

## Function with multiple inputs and input types
def testFunction4(input1,input2,input3):
    print(input1)
    print(input2 + "1") ## will crash if input2 is not a string!
    print(input3 + 1) ## will crash if input3 is not an integer or float!

## Function with string return
def testFunction5(word1,word2):
    combinedWord = word1 + word2
    return combinedWord

## Function with integer return
def testFunction6(factorialThis):
    factorial = 1
    for i in range(1,factorialThis+1):
        factorial = factorial * i
    return factorial

## Students do not need to define functions, but should understand how to call them, input arguments, and recieve/use returned values ## 
## Go through functions individually. Observe and compare the different ways of inputting arguments and outputting results ##

#testFunction1()

#testFunction2("Hello")

#testFunction3(327)

#testFunction4(41231, "testing", 10)

#message = testFunction5("Hello", "World")
#print(message)

#factorial = testFunction6(5)
#print(factorial)
