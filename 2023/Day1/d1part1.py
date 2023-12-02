import re


key = []

file1 = open('2023/Day1/puzzleInput.txt', 'r')

numeric = re.compile(r'[0-9]')

for line in file1:
    extract = numeric.findall(line)
    key.append(extract)


calibrationValue = []

for count in range(len(key)):
    calibrationValue.append(key[count][0] + key[count][-1])

total = 0

for value in range(len(calibrationValue)):
    total += int(calibrationValue[value])

print(f"The sum of all of the calibration values is: {total}")