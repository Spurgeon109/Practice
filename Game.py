import random
if __name__ == '__main__':
    print("Welcome to the game\nGuess a number and enter between 0-9")
    a = int(input())
    b = random.randint(0, 9)
    if a == b: print("You won")
    else: print("You Loss")