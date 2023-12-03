def part01(*, input_name: str = "input") -> int:
    with open(f"C:/Users/jaime/VSCodeProjects/Git/adventofcode2023/calendar/day01/data/{input_name}.txt", "r") as file:
        input = file.read().splitlines()
        
        return sum( # Get the sum of the list
            [
                int(digits[0] + digits[-1]) # 2. Get first and last digit from each list in the digits list (sometimes the same)
                for digits in [
                    [
                        char 
                        for char in lane if char.isdigit() # 1.2 Get each character and test if is a digit
                    ]
                    for lane in input # 1.1 Get each digit of each string from each lane (list)
                ]

            ]
        )

"""
Example
"""    
part01(input_name="part01/example")

"""
Excercise
"""
part01(input_name="input")
