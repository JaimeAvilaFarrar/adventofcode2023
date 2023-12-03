import re

with open("C:/Users/jaime/VSCodeProjects/Git/adventofcode2023/calendar/day01/data/input.txt", "r") as file:
    input = file.read()

input_list = input.split()

input_single_digits_list_of_list = [re.findall(r'\d', input_value) for input_value in input_list]

input_2_digits_list = [
    int(f"{l[0]}{l[-1]}") for l in input_single_digits_list_of_list[-1]
]

result = sum(input_2_digits_list)
result