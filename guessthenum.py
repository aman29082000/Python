ans = 18
c = 9
print("\t\t| GUESS THE NIMBER AND WIN PRIZES |\n")
while (c > 0):

    num = int(input("GUESS THE HIDDEN NUMBER : "))
    c = c - 1
    if num == ans:
        print(" \tWINNNERR !!!!   in  ",(9-c), "Guesses")
        break
    elif num < ans:
        print("\tNUMBER IS LESS ! TRY AGAIN","\tLEFT :", c)
    else:
        print("NUMBER IS GREATER >> TRY AGAIN !!" "\tLEFT :", c)

print("\n\t GAME OVER")