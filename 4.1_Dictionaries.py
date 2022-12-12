# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# A Dictionary Is a mapping Data Type
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.keys())
print("====================Ascessing the Dictionary Items=================")
print()
print("====================Method 1 - By Specifying Key Name==============")
print("Syntax: - dict_name[key_name]")
# Syntax: - dict_name[key_name]
fruits = {
    "Apple's": 5,
    "Orange's": 10,
    "Banana's": 15,
    "Mango's": 20
    }
print(fruits["Banana's"])
print("====================Method 2 - By Get Method==============")
print("Syntax: - dict_name.get(key_name)")
print(fruits.get("Mango"))

print("====================Method 3 - By Keys Method==============")
print("Syntax: - dict_name.keys()")
# keys() ->> This method will return a list of all the keys in the dictionary.
print(fruits.keys())

print("====================Method 4 - By Values Method==============")
print("Syntax: - dict_name.keys()")
# values() ->> This method will return a list of all value names in the dictionary
print(fruits.values())

print("====================Method 5 - By items Method==============")
print("Syntax: - dict_name.items()")
# items() ->> This  method will return each item in a dictionary, as tuples in a list
print(fruits.items())

# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
print("<====================Changing Of Dictionary Items==============>")
print()
print("====================Method-1 By Normal Method ==============")
print("Syntax: - dict_name[Key_name]=Value_name")
orders = {
  "Dosa": 50,
  "Idly": 100,
  "Chapati": 150
}
print("Before ->>",orders)
orders["Puri"] = 200
print("After ->>",orders)
print()
print("<====================Method-2 By Update Method ==============>")
print("Syntax: - dict_name.update({key_name: value})")
# The update() method will update the dictionary with the items like key_name:value pairs
orders.update({"Bondam": 250})
print(orders)
print()

print("<====================Removing Of Dictionary Items==============>")
print()
print("<====================Method 1 POP==============>")
# pop() ->>The pop() method removes the item with the specified key name
print()
print("Syntax:- dict_name.pop(key_name)")
orders.pop("Dosa")
print(orders)
print()
print("<====================Method 2 POP Item==============>")
# The popitem() method removes the last inserted item
print("Syntax:- dict_name.popitem()")
orders.popitem()
print(orders)
print("<====================Method 3 Del==============>")
# The del keyword removes the item with the specified key name
# and also deletes entire Dictionary
print()
print("Syntax:- del dict_name[key_name]\nSyntax:- del dict_name")
del orders["Chapati"]
print(orders)
del orders
# print(orders) # we get Error Because There is No Longer Order Dictionary Available
print("<====================Method 4 Clear Method==============>")
# The clear() method empties the dictionary
print()
print("Syantax:- dict_name.clear()")
university ={
  "CSE": 1600,
  "ECE": 1200,
  "EEE": 1000,
  "ECM": 500
}
university.clear()
print(university)

# ===============================================================================================================================
# ===============================================================================================================================
print("<============================fromkeys() Method=========================>")
# fromkeys() ->> This Method will Help Us to Assign Multiple Keys having a Same Value
print("Syantax:- dict.fromkeys(keys,value)")
student_name = {"Naveen","Virat","Rohit","MSD"}
student_marks = 80
student = dict.fromkeys(student_name,student_marks)
print(student)

person = {
  "Naveen": 18,
  "Rohit": 22
}
person["Naveen"] = 22
print(person)
print(person["Naveen"])