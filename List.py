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
