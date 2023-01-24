import random,time
strt=time.time()
#creating list
list=[]
for i in range(10**4):
	a=random.randrange(10**4)
	if a not in list:
		list.append(a)
print("list is created")
print(f"list has {len(list)} elements in it.")


#list=[72,12,34,61,42,90,4,89,78,59,63,16]

def sort(list):
	lgt=len(list)
	for i in range(1,lgt):
		currNo=list[i]
		prevNo=list[i-1]
		if list[i]<prevNo:
			for j in range(i-1,-1,-1):
				#print(list[i],list[j])   for debugging
				if currNo < list[j]:
					list[i] = list[j]
					list[j] = currNo
					i -= 1
					currNo = list[i]
					#print(list)

sort(list)
end=time.time()
print(list)
print("time taken is",end-strt)