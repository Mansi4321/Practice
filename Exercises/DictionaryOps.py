dict1 = {"Fruit": "Apple", "Vegetable": "Tomato"}

print(dict1.get("vegetable"))
print(dict1.get("Vegetable"))

print(dict1.values())
print(dict1.keys())
print(dict1.items())

dict1.update({"Test": "Automation"})
print(dict1)

keys = ('key1', 'key2', 'key3')
value = 'value2'

dict2 = dict.fromkeys(keys, value)
print(dict2)

