

print("Hello and welcome to my game!")

play=input("do you want to play? (yes or no) ")

if play== "no":
    print("Thank you. We hope that you are able to play in the future. Goodbye")
    quit()

else:
    print("Thank you for accepting to play the game")

    name= input("what is your name? ")

    print(name, "it's good to have you here")

    age=float(input("how old are you (in years)? "))

if age <18:
    print("Sorry, you are not eligible to play the game")
    quit()

else:
    print("Congratulations, you are eligible to play the game")

print(name, "you will be asked 5 questions and provide all answers in small letters")

score=0

Questionone= input("Question 1- what month was Prince George born does? ")

if Questionone=="july":
    print("correct")
    score+=1
else:
    print("incorrect")


Questiontwo= input("Question 2- what does 'He' stand for on the periodic table? ")

if Questiontwo== "helium":
    print("correct")
    score+=1
else:
    print("incorrect")


Questionthree= input("Question 3- what is a baby rabbit called? ")

if Questionthree== "kitten":
    print("correct")
    score+=1
else:
    print("incorrect")


Questionfour= input("Question 4- what is the closest planet to the sun? ")

if Questionfour== "mercury":
    print("correct")
    score+=1
else:
    print("incorrect")


Questionfive= input("Question 5- what is the capital of Iceland? ")

if Questionfive=="reykjavík":
    print("correct")
    score+=1
else:
    print("incorrect")


print ("You have scored", score, "out of", 5)

print("your percentage is", (score/5) *100, "%")


