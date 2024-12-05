with open('Day_1\\Day1_Input.txt', 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        # Split the line into two numbers and add them to their respective lists
        left, right = map(int, line.strip().split()) 
        left_list.append(left)
        right_list.append(right)  


#---Part One---

#Sorting smallest to biggest
left_list.sort()
right_list.sort()

# Calculating the sum of all differences
total_distance = 0
for left, right in zip(left_list, right_list):
    distance_difference = abs(right - left)
    total_distance += distance_difference

# Output the total distance
print("Total Distance:", total_distance)


#---Part Two---

similarity_score = 0
for left in left_list:
    count_in_right = right_list.count(left)  #Count how many times left appears in the right list
    similarity_score += left * count_in_right 

# Output the total similarity score
print("Total Similarity Score:", similarity_score)
