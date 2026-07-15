import random
jackport = random.randint(1,40)
guess = int(input("Enter your number"))
counter = 1
while guess != jackport:
    if guess > jackport:
        print("Guess lower ")
    else:
        print("Guess higher")
    guess = int(input("Enter your number"))
    counter += 1
print("Correct answer")
print("You took",counter,"attempts")














secret=23
chances=5
guess = int(input("Enter your number"))
chances= 1
counter=1
while guess!=secret:
    if guess < secret:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Enter your number"))
    chances+= 1
    counter+=1

print("Correct guess")
print("You took",counter,"attempts")













import random
choices = ["rock","paper","sizer"]
computer = random.choice(choices)
user =  input("Enter rock,paper,sizer").lower()
print("computer chose",computer)
if user == computer:
    print("tie")
elif user == "sizer" and computer == "paper":
    print("you lose")
elif user == "paper" and computer == "rock":
    print("you win")
elif user == "rock" and computer == "sizer":  
    print("you win")
else:
    print("computer win")
    
    


