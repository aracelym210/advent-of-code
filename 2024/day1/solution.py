# create two empty lists for the input
left_list = []
right_list = []

# read in file and split each line into two lists, then sort both lists
with open('input.txt', 'r') as file:
    for line in file:
        left_list.append(line.split()[0])
        right_list.append(line.split()[1])

left_list.sort()
right_list.sort()

""" Part 1 Solution """
# iterate through lists and take the absolute difference between the lists
sum = 0

for index, value in enumerate(left_list):
    diff = abs(int(value) - int(right_list[index]))
    sum += diff

print(sum)

""" Part 2 Solution """
# iterate through numbers in left list and compare with right list
# if the numbers are equal, add plus 1 to the similarity count for the current 
# number on left list. Then multiply by that number and add the product to the total similarity score
total_sim = 0

for num_a in left_list:
    sim_count = 0
    for num_b in right_list:
        if num_a == num_b:
            sim_count += 1

    sim_score = int(num_a) * sim_count
    total_sim += sim_score

print(total_sim)
