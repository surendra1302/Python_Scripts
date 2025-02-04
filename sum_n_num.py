n = int(input("Enter how many numbers you want to sum: "))
sum = 0
for i in range(n):
    sum= sum + i
    print(i)
print(f"Sum of the given {n} numbers: {sum}")
