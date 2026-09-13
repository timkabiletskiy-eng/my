import random

s = 0
def game(s):
    a = random.randint(0, 10)
    i = int(input())
    print(a)
    if i ==a:
        print("you win")
        s+=1
    else:
        print("you lose")
        s += 1
while True:
    game(s)