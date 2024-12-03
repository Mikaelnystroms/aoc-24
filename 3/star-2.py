import re

total_result = 0
enabled = True
input = open("input.txt", "r").read()
x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

for i in x:
    if i == "do()":
        enabled = True
    elif i == "don't()":
        enabled = False
    else:
        if enabled:
            total_result += int(i.split("(")[1].split(",")[0]) * int(i.split(",")[1].strip(")"))

print(total_result)