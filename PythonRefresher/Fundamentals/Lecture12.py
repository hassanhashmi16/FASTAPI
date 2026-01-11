"""
Dictionaires
"""

userDict = {
    "username" : "hassycodes",
    "name" : "hassan",
    "age" : 20
}

# print(userDict["name"])
print(userDict.get("name"))
print(len(userDict))

userDict["married"] = False
print(userDict)

userDict.pop("married")
print(userDict)

userDict.clear()
print(userDict)

# del userDict

for x , y in userDict.items():
    print(x, y )

userDict2 = userDict.copy()
# userDict2 = userDict
userDict2.pop("age")