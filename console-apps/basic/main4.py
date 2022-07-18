#Python Data Structures
#Lists'var = []'
genders = ['male', 'Female', 'Bob Risky', 'James Brown', 'LGBTQ', 'Straight', 'Shemale', 2000, True, False]
print(genders)
print(len(genders))

for gender in genders:
    print(gender)

genders[4] = 'LGBQT'
print(genders)

genders[2:4] = ["Brisky", "Jbrown"]
print(genders)

genders.insert(2, "Undisclosed")
print(genders)

laptopBrands = ["Dell", "Razer Blade", "Asus", "MSI"]
favyBrands = ["Toshiba", "Zinox", "Sony"]
print(laptopBrands)
laptopBrands.append("HP")
print(laptopBrands)
laptopBrands.extend(favyBrands)
print(laptopBrands)

laptopBrands.remove("Dell")
print(laptopBrands)

laptopBrands.pop(5)
print(laptopBrands)

laptopBrands.pop()
print(laptopBrands)

del laptopBrands[1]
print(laptopBrands)

#del laptopBrands
#print(laptopBrands)

l=0
while l < len(laptopBrands):
    print(laptopBrands[l])
    l += 1

print("Using list comprehension")
[print(item) for item in laptopBrands]

laptopBrands.append("1")
print(laptopBrands)

laptopBrands.append("2")
print(laptopBrands)

laptopBrands.reverse()
print(laptopBrands)
laptopBrands.sort(reverse= True)
print(laptopBrands)

laptopBrands.append("Dell")
laptopBrands.append("Dell")
laptopBrands.append("Dell")

print(laptopBrands.count("Dell"))

laptopBrands.clear()
print(laptopBrands)

#Dictionaries - 'var = {key : value, key : value}'
favyFC = {
    "name": "Arsena FC",
    "established": 1905,
    "stadium": "Emirates Stadium",
    "nick": "Gunnerz",
    "cups": ["2004 - PL (Invisibles)", "2020 - FA vs Chelsea"]
}

favyCar = {
    "brand": "Innoson",
    "model": "Ikenga",
    "year": 2021,
    "mileage": 17500,
    "hp": 280
}

print(favyFC["established"])
print(favyFC["name"])
print(favyFC["cups"])

print(len(favyFC))

print(favyFC)

clubName = favyFC.get("name")
print(f"My dearest football club is {clubName}")

thekeys= favyFC.keys()
print(thekeys)

theVals = favyFC.values()
print(theVals)

theItems = favyFC.items()
print(theItems)

#
# for x in favyFC:
#     print(x)
#
# for x in favyCar:
#     print(x)
#
# for x in favyCar.values():
#     print(x)
#
# for x in favyCar:
#     print(favyCar[x])
#
# for x,y in favyCar.items():
#     print(x,y)
#
# if "percentage" in favyCar:
#     print("Yes, this is part of the keys in the dictionary")
# else:
#     print("Please recheck the dictionary")

# print(len(favyCar))

# favyCar["color"] = "black"
# print(favyCar)

# NESTED DICTIONARY
#
# child1 = {
#     "name" : "victory",
#     "year" : 2001
# }
#
# child2 = {
#     "name" : "Glory",
#     "year" : 2003
# }
#
# child3 = {
#     "name" : "Victor",
#     "year" : 2005
# }
#
# child4 = {
#     "name" : "Grace",
#     "year" : 2008
# }
#
#
# mySiblings = {
#     "child1" : child1,
#     "child2" :child2,
#     "child3" :child3,
#     "child4" :child4
# }
# print(mySiblings)
#
# favySeries = dict(title = "unspoken Bond", channel = "starlife", number = 166, time = "10pm" )
# print(favySeries)


