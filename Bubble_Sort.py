import random, time
strt=time.time()
#creating list
list=[]
for i in range(10**4):
	a=random.randrange(10**4)
	if a not in list:
		list.append(a)
print("list is created")
print(f"list has {len(list)} elements in it.")

#sorting the list
def sort():
	global sorted_list,list
	for i in range(len(list)-1):
		n1,n2=list[i],list[i+1]
		if n1>n2:
			list[i+1]=n1
			list[i]=n2
			

for i in range(len(list)):
	sort()
end=time.time()
print(list)
print("time taken is ",end-strt)