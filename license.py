import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
       if file.startswith('LICENSE'):
           print(f"{root}/{file}")
