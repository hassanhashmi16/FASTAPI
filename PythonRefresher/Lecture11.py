"""
loops
"""
myList = [1,2,3,4,5]
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])

for x in myList:
    print(x)

# for i in range(1,5):
#     print(i);
#     i=2 #this wont change the i

sum_of_for_loop = 0
for j in myList:
    sum_of_for_loop += j
print(sum_of_for_loop)

i=0
while i < 5:
    i+=1
    if i ==3:
        continue
    print(i)

    if i==4:
        break
else:
    print(" i is now >= 5")