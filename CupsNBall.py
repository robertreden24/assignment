print("Enter combination of ABCs: ")
input = raw_input()
list = list(input)
cups = ["ball", "empty", "empty"]
x = 0
for x in range(len(list)):
    if list[x] == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif list[x] == "B":
        cups[1], cups[2] = cups[2], cups[1]
    elif list[x] == "C":
        cups[0], cups[2] = cups[2], cups[0]
if "ball" in cups[0]:
    print(1)
elif "ball" in cups[1]:
    print(2)
elif "ball" in cups[2]:
    print(3)

