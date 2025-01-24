my_list = [1, 2, "harish", "devops" , 4 , 5 ]

my_dict = {
            "name":"john",
            "age": 26,
            "city": "Bangalore"
            }

my_list1 = []
if "harish" in my_list:
    print("Element Found")
else:
    print("Element not Found")


if my_list1:
    print("List contains Values")
else:
    print("Empty!!")

print("\n")

if "name" in my_dict:
    print("Key Found")
else:
    print("Key Not Found")
print("\n")

if "name" in my_dict.values():
    print("Value Found")
else:
    print("Value Not Found")

print("\n")
if my_dict["name"] == "harish":
    print("Key contains the value")
else:
    print("Key Not found")

found = True

if not found:
    print("True")
else:
    print("False")

print("\n")

if my_dict:
    print("Dictionary is not empty")
else:
    print("Dict is empty")

