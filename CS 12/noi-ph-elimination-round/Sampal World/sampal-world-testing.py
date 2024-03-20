import sys

test_cases = int(input())

def sampal_game():
    pering = sys.stdin.readline().strip()
    oof = sys.stdin.readline().strip()
    # print(pering, oof)

    choices = ['PAPER', 'SCISSORS', 'ROCK']

    if pering == oof:
        print("TIE")
    
    # normal rock paper scissors
    elif pering in choices and oof in choices:
        if choices[(choices.index(pering) + 1) % len(choices)] == oof:
            print("OOF")
        else:
            print("PLATYPUS")

    # normal rock paper scissors, guns and slap
    elif pering in choices:
        if oof == "SLAP":
            print("PLATYPUS")
        elif oof == "GUNS":
            print("OOF")
    
    # guns and slap, rock paper scissors
    elif pering == "GUNS":
        if oof == "SLAP":
            print("OOF")
        elif oof in choices:
            print("PLATYPUS")
        
    elif pering == "SLAP":
        if oof == "GUNS":
            print("PLATYPUS")
        elif oof in choices:
            print("OOF")

    sys.stdout.flush()

def main():
    for case in range(test_cases):
        sampal_game()

main()