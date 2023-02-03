list = [27, 2, 90, 43, 51, 22]

# DIVIDE FUNCTION#


def divide(list):
    mid = len(list)//2
    L = list[:mid]
    R = list[mid:]
    if len(list) == 1:
        return list
    elif len(list) == 2:
        return merge(L, R)
    elif len(list) > 2:
        out = merge(divide(L), divide(R))
        return out

# MERGE FUNCTION#


def merge(list1, list2):
    list = []
    while len(list1) > 0 and len(list2) > 0:
        e1 = list1[0]
        e2 = list2[0]
        if e1 < e2:
            list.append(e1)
            del list1[0]
        else:
            list.append(e2)
            del list2[0]
    while not (len(list1) == 0 and len(list2) == 0):
        for i in [list1, list2]:
            if len(i) != 0:
                list.append(i[0])
                del i[0]
    return (list)


# CALLING MAIN FUNCTION#
print(divide(list))
