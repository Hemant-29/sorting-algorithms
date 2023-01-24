list = [29, 51, 24, 57, 99, 32, 67, 240, 4, 79, 8, 5, 32, 1]
print("original list:", list)
# sorting the list
def sort():

    global sorted_list, list
    for i in range(len(list) - 1):
        n1, n2 = list[i], list[i + 1]
        if n1 > n2:
            list[i + 1] = n1
            list[i] = n2


for i in range(len(list)):
    sort()
print("sorted list: ", end="")
print(list)
