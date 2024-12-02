levels = []

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        levels.append(list(map(int, line.split())))


def is_safe(report):
    # Check if increasing
    increasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff <= 0 or diff > 3:
            increasing = False
            break
            
    # Check if decreasing 
    decreasing = True
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff <= 0 or diff > 3:
            decreasing = False
            break
            
    # Return true if either increasing or decreasing
    return increasing or decreasing


safe_reports = 0
for report in levels:
    if is_safe(report):
        safe_reports += 1

print(safe_reports)
