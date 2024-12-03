total_result = 0

with open("input.txt", "r") as file:
    input = file.read()

i = 0
while i < len(input):
    if input[i : i + 4] == "mul(":
        i += 4
        num1 = ""
        while i < len(input) and input[i].isdigit():
            num1 += input[i]
            i += 1

        if i < len(input) and input[i] == "," and len(num1) <= 3:
            i += 1
            num2 = ""
            while i < len(input) and input[i].isdigit():
                num2 += input[i]
                i += 1

            if i < len(input) and input[i] == ")" and len(num2) <= 3:
                if num1 and num2:
                    x, y = int(num1), int(num2)
                    if 1 <= x <= 999 and 1 <= y <= 999:
                        total_result += x * y
    i += 1

print(total_result)
