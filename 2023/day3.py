import re

def main():
    lines = []
    with open('inputs/day3-sample.txt', 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())
            
    part1(lines)
    part2(lines)   

def part1(lines):
    """
    - check for numbers or symbol (not period)
    - if number found:
        - get length of number, l 
        - get index of number, i  
        - look left and right for symbol
        - look up and down for symbols in line +/- l starting at i  
    """
    confirmed_part_nums = []
    sum = 0

    for index, line in enumerate(lines):
        print(f"Current line: {line}")
        print(f"Outter most for loop index is {index}")
        potential_part_nums = re.findall(r'\d+', line)

        for p_part_num in potential_part_nums:
            p_part_num_index = line.index(p_part_num)
            
            """edge cases:
                1. part number is at index 0 for line; can't look left
                2. part number is at last index for line; can't look right
                3. first line can't look up
                4. last line can't look down 
            """
            # edge case 1 (can't look left)
            if p_part_num_index == 0:
                look_right(line, p_part_num_index, p_part_num, confirmed_part_nums)
                look_down(lines, index, p_part_num_index, p_part_num, confirmed_part_nums)

            # if able to look right
            elif (p_part_num_index + len(p_part_num)) < len(line): 
                look_right(line, p_part_num_index, p_part_num, confirmed_part_nums)
                look_down(lines, index, p_part_num_index, p_part_num, confirmed_part_nums)
            
            
                
        
        print()

    for n in confirmed_part_nums:
        sum += int(n)
    

def look_right(line, p_part_num_index, p_part_num, confirmed_part_nums):
    print(f"\tLooking right...line is {line}; ppni is {p_part_num_index}; ppn = {p_part_num}")
    char_right = line[p_part_num_index + len(p_part_num)]
    if not char_right.isalnum() and char_right == ".":
        print(f"\tChar_right is not alphanum or a period (.). Char_right is {char_right}")
    else:
        print(f"\tFound a symbol to the right. {char_right}")
        confirmed_part_nums.append(p_part_num)

def look_down(lines, index, p_part_num_index, p_part_num, confirmed_part_nums):
    print("\tTrying to look down...")
    if index >= len(lines) - 1:
        print(f"\tEOF. Can't look down")
    else:
        print(f"\tNext line: {lines[index + 1]}")

    
def part2(lines):
    pass

if __name__ == "__main__":
    main()