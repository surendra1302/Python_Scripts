import random

import sys

import os

print(random.randint(2, 10))


for i in range(2, 10):
    print(i)

print(sys.argv[0])
print(sys.argv[1])
print(sys.path)

os.chdir("/home/ubuntu")
os.makedirs("/home/ubuntu/newdir", exist_ok=True)
os.chdir("/home/ubuntu/newdir")
print(os.getcwd())

os.listdir("/home/ubuntu")
print(os.listdir("/home/ubuntu"))
print(os.listdir("/home/ubuntu/python"))

for path, dir, files in os.walk("/home/ubuntu"):
    print(path, dir, files)

