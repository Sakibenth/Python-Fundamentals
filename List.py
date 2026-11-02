l=[1,2,3,4,1]
print(l)
print(len(l)) #len of the list
print(l.count(1))
print(l.count(5))
print(l.index(1)) #returns the index of the first ocurance
# print(l.index(5)) 5 is not in the list
value=(int)(input("Enter the value:"))
if value in l:
    print('{} is available at index: {}'.format(value,l.index(value)))
else:
    print(value," is not in the list")
#append,insert
l.append(10)
l.append(20)
l.append(30)
print(l)
l2=[]
for i in range(1,101):
    if i%10==0:
        l2.append(i)
print(l2)
l2.insert(5,101) #at 5th index,101 will be put and the rest of the element will shift right
print(l2)
l2.insert(len(l),110)  #inserting 110 at the end of the list. That's what append does
print(l2)

