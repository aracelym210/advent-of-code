"""
    author: aracelym
    date: 12/10/23

    problem: Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
            one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

            Equipped with this new information, you now need to find the real first and last digit on each line. For example:

            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen

            In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

            What is the sum of all of the calibration values?
    
    refs: used ChatGPT to help identify logic flaws I was running into with first attempt at a solution

"""
import re

def main():
    lines = read_lines('inputs/day1a.txt')
    mod_lines = []

    for line in lines:
        if line.isdigit():
            mod_lines.append(line)
        else:
            cleaned_line = clean_line(line)
            mod_lines.append(cleaned_line)
        
    add(extract_digits(mod_lines))

def read_lines(filename):
    """
        Read lines and strip out newline characters 
    """
    lines = [] 
    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    for line in raw_lines:
        lines.append(line.strip())
    
    return lines

def clean_line(line):
    number_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Create a regex pattern to match number words. Equivalent to one|two|three... etc
    #pattern = re.compile('|'.join(number_map.keys()))
    pattern = re.compile(r'(?:' + '|'.join(number_map.keys()) + r')')
    #pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

    # Replace each matched number word with its corresponding digit using a nested function
    def replace(match):
        word = match.group(0)
        print(word)
        return str(number_map[word])

    # the regex pattern object's method "sub" can take either a string or function as it's 
    # first argument. Here, we reference the replace method defined above 
    cleaned_line = pattern.sub(replace, line)

    print(f"Original line: {line}")
    print(f"Cleaned line: {cleaned_line}\n\n")

    return cleaned_line


def extract_digits(mod_lines):
    clean_digits = []
    #print(mod_lines)
    for digit in mod_lines:
        print(digit)
        #print("digit: {digit}")
        # clean_digits.append(re.findall(r'\d', digit)) --> 53363
        clean_digits.append(re.findall(r'\d{1}', digit))
    return clean_digits

def add(clean_digits):
    sum = 0
    for num in clean_digits:
        #print(num)
        if len(num) > 1:
            #print(f"Adding {int(num[0] + num[-1])}")
            sum += int(num[0] + num[-1])
        if len(num) == 1:
            #print(f"Adding {int(num[0][0] + num[0][-1])}\n")
            sum += int(num[0][0] + num[0][-1])

    print(sum)

if __name__ == '__main__':
    main()