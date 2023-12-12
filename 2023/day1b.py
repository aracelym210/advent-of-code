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

def main():
    lines = read_lines('inputs/day1b-sample.txt')
    print(lines)

    cleaned_lines = str_to_digit_handler(lines)

    print(cleaned_lines)

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

def str_to_digit_handler(lines):
    """
        Using a series of if statements, iterate through each line apply 
        fixes when necessary 

        Returns a new list with cleaned values to later be used for extracting and 
        summing values
    """
    values_to_extract = []
    for line in lines:
        if line[0].isdigit() and line[-1].isdigit():
            values_to_extract.append(line)
            #print("first and last characters are digits.")
        else:
            cleaned_line = str_to_digit(line)
            values_to_extract.append(cleaned_line)
            #print(f"niether the first or last characters are digits.")

    return values_to_extract


def str_to_digit(line):
    """
        sort number map so that we check for longer length number strings before shorter ones
        this will handle edge cases like eightwothree != eight2three since "two" is before "eight" in number_map
        str_num[0] refers to the first element in the tuple. (i.e. (one, 1) -> str[0] == one)
    """
    number_map = { 'one':1, 'two': 2, 'three':3 , 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
    sorted_numbers = sorted(number_map.items(), key= lambda str_num: len(str_num[0]), reverse=True)

    clean_line = line
    for string_num, number in sorted_numbers:
        clean_line = clean_line.replace(string_num, str(number))
    
    return clean_line


def generate_cv_array(lines):
    """
        This function exists only to append values to array
        Value extraction handled in separate function extract_calibration_values()
    """
    calibration_values = []
    
    # if line does not have numbers, skip extraction (i.e. eighttwothree)
    for line in lines:
        if line.isalpha():
            continue
        else:
            c_value = extract_calibration_values(line)
            calibration_values.append(c_value)

    return calibration_values


def extract_calibration_values(line):
    """
        Looks for first digit in line(str) and appends to temp variable
        Then looks for the last digit by iterating through the line in reverse and appends that
        to the same temp variable
    """
    c_value = ''
    reverse = line[::-1]

    for char in line:
        if char.isdigit():
            c_value += char
            break 

    for char in reverse:
        if char.isdigit():
            c_value += char
            break     
    
    c_value = int(c_value)
    
    return c_value


def add_calibration_values(calibration_values):
    sum = 0

    for value in calibration_values:
        sum += value

    return sum



                

if __name__ == '__main__':
    main()