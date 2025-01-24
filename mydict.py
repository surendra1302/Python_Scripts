mydict={
        "name": "surendra",
        "id": 1234,
        "domain": ["devops", "cloud engineer", "SRE"],
        "tools": {
            "os": ["linux", "windows"],
            "cloud": "AWS"
            }
        }
print(mydict)
print(mydict["name"])
print(mydict["domain"])
print(mydict["tools"])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][1])

mydict1={
        "name1": "satya",
        "id1": 6789
        }
print(mydict1)
mydict.update(mydict1)
print(mydict)
mydict["place"]="bangalore"
print(mydict)
mydict["Place"]=["bangalore", "pune"]
print(mydict)
