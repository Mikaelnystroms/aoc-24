left_list = []
right_list = []

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

right_counts = {}
for num in right_list:
    if num in right_counts:
        right_counts[num] += 1
    else:
        right_counts[num] = 1

similarity_score = 0
for left_num in left_list:
    right_count = right_counts.get(left_num, 0)
    similarity_score += left_num * right_count

print(similarity_score)
