def new_game():
    guesses = []
    correct_answer = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]: #o -1 é porque começou em 1, mas toda linguagem conta a partir do zero
            print(i)
        guess = input("Enter (A, B or C): ")
        guess = guess.upper()
        guesses.append(guess)
        print("----------------------------")
        correct_answer += check_answer(questions.get(key),guess) #O método get pega o value de uma key 
        print("----------------------------")
        question_num+=1

    score(correct_answer, guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Right!!")
        return 1
    else:
        print("Wrong!!")
        return 0
def score(total, guesses):
    print("You answered "+str(total)+" questions correctlly")

    print()
    print("ANSWERS: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ",end="")
    for i in guesses:
        print(i, end=" ")

    play_again()
def play_again():
    resp = input("\nQuer jogar de novo? (S/N): ")
    if(resp.upper() == "S"):
        print("----------------------------")
        new_game()
    else:
        return
    
#dicionario
questions = {
    "Who won the first World Cup: " : "C",
    "How many ballons d'or has Lionel Messi: " : "C",
    "Who won the COPA DO BRASIL in 2014: " : "C",
    "When Internacional relegated to the second division: " : "B",
}

#2d list
options =[
    ["A. Brazil","B. Argentina","C. Uruguay"],
    ["A. 9","B. 7","C. 8"],
    ["A. Cruzeiro","B. Corinthians","C. Galo"],
    ["A. 2018","B. 2016","C. 2017"]
]

new_game()