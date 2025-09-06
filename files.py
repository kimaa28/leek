#!/usr/bin/python3

print("hello e world")
print("je suis  deja la")
my_list = {}
print(my_list)

my_list["hello"] = {"hello": "je suis deja la", "patou": "est un gros lard"}
print(my_list)
for value in my_list.values():
	print(value)
	datei = value["hello"]
	daten = value["patou"]
	print(datei, daten)

liste = [f"lektion{i}" for i in range(5)]

for i in liste :
    print(i, "je suis un gros con")
    
