def part_one_is_safe(report):
    #increasing or decreasing check
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    # Check if levels differ by 1 to 3
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            return False
    
    return increasing or decreasing

def part_two_is_safe(report):
    #Check if the report is already safe
    if part_one_is_safe(report):
        return True
    
    #Check if removing any single element makes it safe
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:] 
        if part_one_is_safe(new_report):
            return True
    
    # If no removal results in a safe report, it's still unsafe
    return False

def count_safe_reports_1():
    safe_count = 0
    
    with open('Day_2\\Day2_Input.txt', 'r') as file:
        for line in file:
            # Convert each line into a list of integers
            report = list(map(int, line.split()))
            #Check if the report is safe
            if part_one_is_safe(report):
                safe_count += 1
    
    return safe_count

def count_safe_reports_2():
    safe_count = 0
    
    with open('Day_2\\Day2_Input.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            # Check if the report is safe with new conditions
            if part_two_is_safe(report):
                safe_count += 1
    
    return safe_count

print('Part One: ', count_safe_reports_1())
print('Part Two: ', count_safe_reports_2())
