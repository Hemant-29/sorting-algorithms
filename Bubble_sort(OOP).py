list = [29, 51, 24, 57, 99, 32, 67, 240, 4, 79, 8, 5, 32, 1]

# sorting the list


class sort:
    def __init__(self, list, type=""):
        self.list = list

        if "bubble" in type.lower():

            for i in range(len(list)):

                self.bubble_sort()

    def bubble_sort(self):

        for i in range(len(list) - 1):

            n1 = list[i]

            n2 = list[i + 1]

            if n1 > n2:

                list[i + 1] = n1

                list[i] = n2


sort(list, "BuBBle")

print(list)
