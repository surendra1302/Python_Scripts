num = int(input("Enter a number to see its multiplication table (1-9): "))

print(f"Multiplication Table of {num}:")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")
