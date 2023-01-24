list = [72, 12, 34, 61, 42, 90, 4, 89, 78, 59, 63, 16]


def sort(list):
    lgt = len(list)
    for i in range(1, lgt):
        currNo = list[i]
        prevNo = list[i - 1]
        if list[i] < prevNo:
            for j in range(i - 1, -1, -1):
                # print(list[i],list[j])   for debugging
                if currNo < list[j]:
                    list[i] = list[j]
                    list[j] = currNo
                    i -= 1
                    currNo = list[i]
                    # print(list)


sort(list)
print(list)
