import random

x = random.randint(1,6) #an int number between 1 'n 6
y = random.random()
print(x)
print(y)

myList = ["rock", "paper", "scissors"]

escolha = input("Your choice: ")
z = random.choice(myList)
print("Computer choice: "+z)

#while True:

if(escolha == "rock" and z == "scissors"):
    print("You win")
elif(escolha == "rock" and z == "paper"):
    print("You lose")
elif(escolha == "paper" and z == "rock"):
    print("You win")
elif(escolha == "paper" and z == "scissors"):
    print("You win")
elif(escolha == "scissors" and z == "rock"):
    print("You lose")
elif(escolha == "scissors" and z == "paper"):
    print("You win")
else:
    print("It's a tie")
    
 

cards = [1,2,3,4,5,6,7,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
