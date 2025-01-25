import os

# Define the output file
output_file = "1.txt"

# Clear the output file if it already exists
with open(output_file, "w") as f:
    f.write("")  # Empty the file

# Iterate over all directories and files starting from the specified directory
for root, dirs, files in os.walk("/home/ubuntu/"):
    for file in files:
        # Check if the file starts with 'LICENSE'
        if file.startswith("LICENSE"):
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")

            # Open the file and read its content
            with open(file_path, "r") as fh:
                content = fh.read()

                # Display the file name and its content
                print(f"Content of {file_path}:\n{content}\n")

                # Append the content to the output file
                with open(output_file, "a") as output:
                    output.write(f"--- {file_path} ---\n")
                    output.write(content)
                    output.write("\n\n")

print(f"All LICENSE files have been aggregated into {output_file}.")

