f = open("f_libraries_of_the_world.txt", "r")

books,library,days=f.readline().split()
books=int(books)
library=int(library)
days=int(days)
scores=list(map(int,f.readline().split()))
lib_att=list()
arr_book=list()
for i in range(library):	
	temp=list(map(int,f.readline().split()))
	temp.append(i)
	#lib_att.append(temp)
	temp1=list(map(int,f.readline().split()))
	sum=0
	for l in range(len(temp1)):
		#print(temp1[l])
		sum=sum+scores[temp1[l]]
		#sum=sum+(arr_book[(temp1[l])])
	demo=sum//temp[1]
	temp1.append(demo)
	for z in temp1:
		temp.append(z)
	lib_att.append(temp)

#print(*lib_att)
tt=open("f.txt", "w")
lib_att.sort(key = lambda x: x[-1],reverse=True)
count=0
sum_days=0
for j in range(library):
	if(sum_days+lib_att[i][1]<=days):
		count=count+1
print(count,file=tt)
for k in range(count):
	print(lib_att[k][3],end=" ",file=tt)
	print(len(lib_att[k])-4,file=tt)
	print(*lib_att[k][4:],file=tt)



#arr_book.append(temp1)
"""
sum_days=0
lib_index=list()
for i in reversed(range(library)):
	if (sum_days+lib_att[i][1]<=days):
		lib_index.append(i)
		sum_days=sum_days+lib_att[i][1]

tt=open("f.txt", "w")
print(len(lib_index),file=tt)
for j in lib_index:
	print(j,end=" ",file=tt)
	print(len(arr_book[j]),file=tt)
	print(*arr_book[j],file=tt)
"""