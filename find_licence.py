license_file = "/home/ubuntu/LICENSE"
output_file = "/home/ubuntu/copyright.txt"

try:
    
    with open(license_file, "r") as file:
        content = file.readlines()

    with open(output_file, "a") as output:  
        for line in content:
            if "copyright" in line.lower():  
                output.write(line)

    print(f"Matching lines appended to {output_file}")

except FileNotFoundError:
    print(f"Error: File {license_file} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
