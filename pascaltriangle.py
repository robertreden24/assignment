print("Enter height of pascal triangle: ")
rows = int(input())
pascal_triangle = [1]
for i in range(rows):
    print(pascal_triangle)
    list = []
    list.append(1)
    for j in range(len(pascal_triangle) - 1):
        list.append(pascal_triangle[j] + pascal_triangle[j + 1])
    list.append(1)
    pascal_triangle = list