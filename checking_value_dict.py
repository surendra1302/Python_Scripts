mydict={
        "name": "surendra",
        "id": 1234,
        "place": "banglore"
        }
if(mydict):
    print("the dictionary is not empty")

else:
    print("the dictionary is empty")

if "surendra" in  mydict.values():
    print("the value is present")

else:
    print("the value is not present")

if "name" in mydict.keys():
    print("the key is present")
else:
    print("the key is not present")

if mydict["name"] == "surendra":
    print("key and value are matching")
else:
    print("key and value do not match")
