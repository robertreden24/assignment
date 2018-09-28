print("How many numbers do you want to input?")
n = int(input())
t = 0
while t<n:
    i = int(input())
    t = t + 1
    if i % 2 == 0:
        print("Bob wins")
    else:
        print("Alice wins")