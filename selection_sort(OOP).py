list=[71,91,46,61,92,89,58,10,4,2,40,97]
print("original list: ",list)

#sorting the list
indx=0
def sort(list):
	global indx
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

for i in range(len(list)):
	sort(list)
print("sorted list: ",end="")
print(list)
