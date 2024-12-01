left_list = []
right_list = []

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

distances = []
for left, right in zip(sorted_left, sorted_right):
    distance = abs(right - left)
    distances.append(distance)

total_distance = sum(distances)

print(total_distance)
