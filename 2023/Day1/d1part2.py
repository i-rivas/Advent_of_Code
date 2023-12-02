def convert_word_to_digit(word):
    """ Convert word representation of a digit to its numerical value. """
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    return word_to_digit.get(word, "")

def sum_calibration_values_part_two(lines):
    total_sum = 0
    for line in lines:
        line = line.strip()

        # Finding digits and words representing digits
        digits = []
        word = ""
        for char in line:
            if char.isdigit():
                if word:  # If a word is formed, check if it's a valid digit word
                    digit = convert_word_to_digit(word)
                    if digit:
                        digits.append(digit)
                    word = ""
                digits.append(char)
            elif char.isalpha():
                word += char
                if word in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
                    digits.append(convert_word_to_digit(word))
                    word = ""

        if len(digits) >= 2:
            # Combine the first and last "digit" to form a two-digit number
            total_sum += int(digits[0] + digits[-1])

    return total_sum

# Usage
# lines = [line1, line2, ...]  # Your input data
# sum_calibration_values_part_two(lines)
file1 = open('2023/Day1/puzzleInput.txt', 'r')

print(sum_calibration_values_part_two(file1))