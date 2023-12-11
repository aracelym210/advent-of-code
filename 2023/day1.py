"""
    author: aracelym
    date: 12/10/23

    problem: The newly-improved calibration document consists of lines of text; 
             each line originally contained a specific calibration value that the Elves now need to recover. 
             On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
             to form a single two-digit number.

            For example:

            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet

            In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

            Consider your entire calibration document. What is the sum of all of the calibration values?
"""

def main():
    lines = read_input('inputs/day1a.txt')

    calibration_values = generate_cv_array(lines)

    sum = add_calibration_values(calibration_values)

    print(sum)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    return lines


def generate_cv_array(lines):
    """
        This function exists only to append values to array
        Value extraction handled in separate function extract_calibration_values()
    """
    calibration_values = []
    
    for line in lines:
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