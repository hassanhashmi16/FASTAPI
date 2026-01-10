"""
Lists
"""

myList = [100, 90 , 70, 80 , "Hi"]
print(myList)

myList[0] = "now"
print(myList[-1])
print(myList[0])
print(len(myList[-1]))
print(len(myList))

#print 0 till 2 but dont print 2
print(myList[0:2])
print(myList[:2])
print(myList[1:])

myList.append(1000)
print(myList)
myList.insert(1,2000)
print(myList)
myList.remove(70)
myList.pop()
print(myList)
myList.pop(0)
print(myList)
#wont work because int and str both are present in a single list
myList.sort()
print(myList)