my_dict = {
           "name": "john",
           "age": 25,
           "city": "Bangalore"
           }


for key in my_dict.keys():
    print(key)

print("\n")

for value in my_dict.values():
    print(value)

print("\n")

for key,value in my_dict.items():
    print(key, value)
