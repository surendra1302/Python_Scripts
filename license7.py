import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
       if file.startswith('LICENSE'):
           print(f"{root}/{file}")

with open(file,"r") as fh:
    content = fh.read()

    print(f"Content of {file}:\n{content}\n")

with open(output_file,"a") as fh1:
    fh1.write(f"{file}\n")
    fh1.write(content)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import os

for root, dir, files in os.walk("/home/ubuntu/python"):
    for file in files:
       if file.startswith('LICENSE'):
           print(f"{root}/{file}")

           with open(file,"r") as fh:
            content = fh.read()

            # Display the file name and its content
            print(f"Content of {file}:\n{content}\n")

            # Append the content to the output file
            with open(output_file,"a") as fh1:
                fh1.write(f"{file}\n")
                fh1.write(content)

