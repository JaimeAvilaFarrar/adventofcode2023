import re

# Set input
data_file_name = 'input'
# data_file_name = 'part02/example'

# Read input
with open(f"C:/Users/jaime/VSCodeProjects/Git/adventofcode2023/calendar/day01/data/{data_file_name}.txt", "r") as file:
    input = file.read()

# Split input in diff lines lists
input_list = input.split()

# Mapping str digits to int
digits_mapping = {
    "one": "1",
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7", 
    "eight": "8", 
    "nine" : "9"
}

# Setting regex to recover digits
str_digits_regex_pattern = '|'.join(digits_mapping.keys())
int_digits_regex_pattern = '\d'
regex_pattern = f"(?=({str_digits_regex_pattern}|{int_digits_regex_pattern}))"

# Recover digits & str numbers for each line
list_of_line_digits = [re.findall(regex_pattern, input_value) for input_value in input_list]

# Transform str numbers into their digit equivalent
transformed_list_of_line_digits = [
    [e if e.isdigit() else digits_mapping[e] for e in line_list_elements] # Transform str into int digits
    for line_list_elements in list_of_line_digits
]

# Recover first and last digit of
int_digits_by_lane_list = [int(d[0] + d[-1]) for d in transformed_list_of_line_digits]

# Get response through sum
response = sum(int_digits_by_lane_list)

# Output for advent of code
print(f"response: {response}")