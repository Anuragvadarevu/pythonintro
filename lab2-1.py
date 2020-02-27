numlist=[2,3,4,88,535,345,1,16]

x= sum(numlist)/len(numlist)
print(float(x))

numlist.pop(4)
x= sum(numlist)/len(numlist)
print(float(x))

