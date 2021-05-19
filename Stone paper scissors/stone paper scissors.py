print ("GAME: stone paper scissor ")
a = input("1st player turn : ")
b = input("2nd player turn : ")


if a == b:
    print(" The game is a tie")
elif a == "stone" and b == "paper":
    print("Player 2 wins")
elif a == "paper" and b == "scissor":
    print("Player 2 wins")
elif a == "scissor" and b == "stone":
    print("Player 2 wins")
else:
    print("player 1 wins")


#print(f"player 1 choose : {a}")
#print(f"player 2 choose : {b}")
