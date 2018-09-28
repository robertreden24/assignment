print("Input 10 numbers: ")
x = 10
while(x != 0):
    list = []
    for i in range(10):
        num = int(input())
        if num % 42 not in list:
            list.append(num % 42)
    print(len(list))
    x = x - 1
    break