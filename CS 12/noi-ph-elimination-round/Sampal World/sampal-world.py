import sys

def sampal_game():
    pering = sys.stdin.readline().strip()
    oof = sys.stdin.readline().strip()

    choices = ['PAPER', 'SCISSORS', 'ROCK']

    if pering == oof:
        print("TIE")
    
    elif pering in choices and oof in choices:
        if choices[(choices.index(pering) + 1) % len(choices)] == oof:
            print("OOF")
        else:
            print("PLATYPUS")

    elif pering in choices:
        if oof == "SLAP":
            print("PLATYPUS")
        elif oof == "GUN":
            print("OOF")
    
    elif pering == "GUN":
        if oof == "SLAP":
            print("OOF")
        elif oof in choices:
            print("PLATYPUS")
        
    elif pering == "SLAP":
        if oof == "GUN":
            print("PLATYPUS")
        elif oof in choices:
            print("OOF")

    sys.stdout.flush()

sampal_game()