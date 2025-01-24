mylist=[10, 134, 33, 54, 26, 44, 102, 65, 15]

print("the original list is:",mylist)

for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i]>mylist[j]:
            temp=mylist[i]
            mylist[i]=mylist[j]
            mylist[j]=temp
print("the ascending order of list:",mylist)
