list = [72, 12, 34, 61, 42, 90, 4, 89, 78, 59, 63, 16]
# sorting the list


class sort:
    def __init__(self, list, type=""):
        self.list = list
        if "insertion" in type.lower():
            self.insertion_sort()

    def insertion_sort(self):
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


sort(list, "insertion")
print("sorted list:", list)
