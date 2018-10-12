# Exercise 8 (Rock Paper Scissors)
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# Main Code
check = "yes"
while check == "yes":
    player1 = input("Player 1 uses ")
    player2 = input("Player 2 uses ")

    if player1 == player2:
        print("Draw")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins")

    check = input("Do you want to play a new game? ")
