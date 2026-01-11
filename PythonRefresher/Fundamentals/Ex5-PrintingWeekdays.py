myList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i=0
while i < 3 :
    for j in myList:
        if j == "Monday":
            continue
        print(j)
    i+=1



"""My practice : Printing a pattern of stars on 5 lines"""

row = 1

while row <= 5:
    col =1
    while col <= row:
        print("*" , end="")
        col +=1
    print()
    row+=1

for i in range(5):
    for j in range(5):
        if(j<=i):
            print("*" , end="")
    print()

for i in range(1,6):
    print("*"*i)

for i in range(5 , 0, -1):
    print("*"*i)

rows = 5
for i in range(1 , rows+1 ):
    print(" "*(rows-i) + "*"*(2*i-1))
