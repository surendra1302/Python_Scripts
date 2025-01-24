import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.startswith('NOTICE'):
            print(f"{root}/{file}")
