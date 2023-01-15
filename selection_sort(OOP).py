list=[71,91,46,61,92,89,58,10,4,2,40,97]
print("original list: ",list)

#sorting the list


class sort():
	def __init__(self,list,type=""):
	self.indx=0
		if "select" in type.lower():
			for i in range(len(list)):
				selction_sort()

	def selection_sort(self):
		indx=self.indx
		list=self.list()
		min=10**100
		#finding minimum
		for i in range(indx,len(list)):
			if list[i] < min:
				min = list[i]
				indx_min = i
		#swapping
		list[indx_min] = list[indx]
		list[indx]=min
		indx+=1


print("sorted list: ",end="")
print(list)
