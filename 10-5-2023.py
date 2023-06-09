#  Python Code to get the minimun efficiency
efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

efficiency.sort(reverse=True)

results = []
diff= []
sum = []
total_cost = []

for i in range(len(efficiency)):
    temp_arr = efficiency[:i] + efficiency[i+1:]
    results.append(sorted(temp_arr))
for sub_list in results:
    pairs = []
    # Iterate over each element in the sub-list in pairs using zip function
    for x, y in zip(sub_list[0::2], sub_list[1::2]):
        pairs.append((x, y))
    diff.append(pairs)
for sub_list in diff:
    abs_diff = []
    # Iterate over each pair in the sub-list and calculate the absolute difference
    for pair in sub_list:
        diff = abs(pair[0] - pair[1])
        abs_diff.append(diff)
    sum.append(abs_diff)

for sub_list in sum:
    total = 0
    # Iterate over each element in the sub-list and calculate the sum
    for num in sub_list:
        total += num
    total_cost.append(total)
min_cost = min(total_cost)

print("min: ", min_cost)