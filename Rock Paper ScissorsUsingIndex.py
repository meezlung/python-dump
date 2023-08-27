def rps(p1, p2):
    l = ["rock", "paper", "scissors"]
    newP1 = l.index(p1)
    newP2 = l.index(p2)
    difference = newP1 - newP2
    if difference > 0:
        return "Player 1 won!"
    if difference == 0:
        return "Draw!"
    if difference < 0:
        return "Player 2 won!"

print(rps("rock","paper"))