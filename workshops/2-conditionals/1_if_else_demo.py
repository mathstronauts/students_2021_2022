number1 = 100

if number1 > 90:
    print("Number1 is > 90!")
elif number1 > 70:
    print("Number1 is > 70!")
else:
    print("Number1 is < 90 and  Number is < 70!")

number2 = 100
if number2 > 50 and number2 < 150:
    print("Number2 is between(non-inclusive) 50 and 150!")

number3 = 100
if number3 % 2 == 0 or number3 % 3 == 0:
    print("Number3 is a multiple of 2 or 3!")

## If statements with input() function ##
password = "open sesame"
inputedWord = input("Enter password: ")

if inputedWord != password:
    print("Incorrect password!")
else:
    print("Correct password!")
