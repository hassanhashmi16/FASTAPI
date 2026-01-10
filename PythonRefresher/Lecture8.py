"""
sets and tuples
"""
'''sets can not have duplicates and are unordered'''

mySet = {1,2,3,4,5,1,7,6}
# print(mySet)
# print(len(mySet))
#
# for x in mySet:
#     print(x)
#
# # print(mySet[0]) error
#
# mySet.discard(5)
# print(mySet)
#
# # mySet.clear()
# print(mySet)
#
# mySet.add(8)
# print(mySet)
#
# mySet.update([9,10])
# print(mySet)



"""TUPLES"""
myTup = (1,2,3,4,5)
print(myTup[2])
myTup2 = (6,7,8,9,10)
myTup.__add__(myTup2)
print(myTup)
print(myTup2)