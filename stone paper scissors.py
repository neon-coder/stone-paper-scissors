import random
moves = ["rock", "paper", "scissors"]
keep_playing = "true"
while keep_playing == "true":
    cmove = random.choice(moves)
    pmove = input("What is your move: rock, paper or scissors?")
    print ("The computer chose",cmove)
    if cmove == pmove:
        print ("Tie")
    elif pmove == "rock" and cmove == "scissors":
        print ("Player wins")
    elif pmove == "rock" and cmove == "paper":
        print ("Computer wins")
    elif pmove == "paper" and cmove == "rock":
        print ("Player wins")
    elif pmove == "paper" and cmove == "scissors":
        print ("Computer wins")
    elif pmove == "scissors" and cmove == "paper":
        print ("Player wins")
    elif pmove == "scissors" and cmove == "rock":
        print ("Computer wins")
