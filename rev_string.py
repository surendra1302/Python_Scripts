string=input("Enter the string to reverse\n")
reverse=""

for char in string:
    reverse=char + reverse

print(reverse)
