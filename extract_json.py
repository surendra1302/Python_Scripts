import json
import requests
import tarfile
import sys
with open("/home/ubuntu/python/sample.json", "r") as fh:
    json_data=json.load(fh)
   # print(json_data)

#for ele in json_data:
 #   for key,value in ele.items():
  #      print(key)
   #     print(value)
    #    print("-----------")

file_path="/home/ubuntu/python/behave.tar.gz"
for ele in json_data:
    #print(ele["Source URL"])
    source_url=ele["Source URL"]
    response = requests.get(source_url)
   # response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("Tar file downloaded successfully.")
    break
file = tarfile.open('/home/ubuntu/python/behave.tar.gz') 
file.extractall('/home/ubuntu/python') 
sys.exit()
