list = [71, 91, 46, 61, 92, 89, 58, 10, 4, 2, 40, 97]

# sorting the list


class sort:
    def __init__(self, list, type=""):
        self.indx = 0
        self.list = list
        if "select" in type.lower():
            for i in range(len(list)):
                self.selection_sort(self.indx)

    def selection_sort(self, indx):
        min = 10**100
        # finding minimum
        for i in range(indx, len(list)):
            if list[i] < min:
                min = list[i]
                indx_min = i
        # swapping
        list[indx_min] = list[indx]
        list[indx] = min
        self.indx += 1


sort(list, "selection")
print("sorted list: ", end="")
print(list)
