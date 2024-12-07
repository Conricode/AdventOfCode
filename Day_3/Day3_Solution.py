import re

#Part One
def process_instructions(file_path):
    total_sum = 0
    # Define a regex pattern: mul(X,Y) with valid numbers inside
    pattern = r"mul\((\d+),(\d+)\)"
    
    with open(file_path, 'r') as file:
        content = file.read() 
        
        # Find all matches for the pattern
        matches = re.findall(pattern, content)
        
        # Process each match and multiply the numbers for total sum
        for match in matches:
            x = int(match[0])
            y = int(match[1])
            total_sum += x * y
    
    return total_sum

#Part Two
def process_instructions_with_conditions(file_path):
    total_sum = 0
    is_enabled = True  # Initially, mul instructions are enabled

    instruction_pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")  # Matches valid instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")  # Matches mul(X, Y)

    with open(file_path, 'r') as file:
        content = file.read()

        # Extract only valid instructions
        instructions = instruction_pattern.findall(content)
        for instruction in instructions:
            # Check for do() or don't() instructions
            if instruction == "do()":
                is_enabled = True
            elif instruction == "don't()":
                is_enabled = False
            else:
                # Process mul(X, Y) instructions
                mul_match = mul_pattern.match(instruction)
                if mul_match:
                    x = int(mul_match.group(1))
                    y = int(mul_match.group(2))
                    if is_enabled:
                        total_sum += x * y

    return total_sum



file_path = 'Day_3\\Day3_Input.txt'

result_part_one = process_instructions(file_path)
print('Part 1: ', result_part_one)

result_part_two = process_instructions_with_conditions(file_path)
print('Part 2: ', result_part_two)
