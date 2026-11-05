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
l2.insert(len(l2),110)  #inserting 110 at the end of the list. That's what append does
print(l2)
#extend 
order_1=['chicken','mutton','fish']
order_2=['broiler','black_bengal','rui']
order_1.extend(order_2)
print(order_1)
#append vs extend
l1=[10,20,30]
l2=[40,50]
l1.append(l2)
print(l1) #[10,20,30,[40,50]]
print(len(l1)) #4

l1=[10,20,30]
l2='abc'
l1.append(l2)
print(l1) #[10,20,30,'abc']
l1.extend(l2)
print(l1) #[10,20,30,'abc','a','b','c']

#remove
l1=[10,20,10,20,40]
l1.remove(40)
print(l1)
l1.remove(10)
print(l1) #[20,10,20] #first occurance of 10 is removed
#l1.remove(50) if the element is not in list then we will get value error

#pop : remove and return the element at last index or specific index
l=[10,20,30]
print(l)
print(l.pop()) 
print(l)
#with argument
l=[10,20,40]
print(l.pop(1))
print(l)