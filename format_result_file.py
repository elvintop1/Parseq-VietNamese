import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Replace '\\t' with space in a text file")

# Add arguments for input and output file paths
parser.add_argument("input_file", help="Path to the input text file")
parser.add_argument("output_file", help="Path to the output text file")

# Parse the command-line arguments
args = parser.parse_args()

# Read the input text file
with open(args.input_file, "r") as input_file:
    input_lines = input_file.readlines()

# Process the input lines, separating image path and label with a space
output_lines = []
error_lines = []
for line_number, line in enumerate(input_lines, start=1):
    parts = line.strip().split('\t')
    if len(parts) == 2:
        image_name, label = parts
        modified_line = f"{image_name} {label}\n"
        output_lines.append(modified_line)
    else:
        image_name = parts[0]
        modified_line = f"{image_name} -\n"
        output_lines.append(modified_line)
        error_lines.append(f"Label missing in line {line_number}: {line}")

# Write the modified text to the output file
with open(args.output_file, "w") as output_file:
    output_file.writelines(output_lines)

print(f"Text from {args.input_file} has been processed and saved to {args.output_file}.")

# Count the number of lines in the output file
with open(args.output_file, "r") as output_file:
    line_count = sum(1 for line in output_file)
if line_count == 33000:
    print(f"Number of lines in {args.output_file}: {line_count} / 33000")
else : 
    print("Error (x)")
# Check for lines with missing labels and print errors
if error_lines:
    print("\nErrors (lines with missing labels):")
    for error_line in error_lines:
        print(error_line)
else: 
    print(f"File {args.output_file} is qualified !")
