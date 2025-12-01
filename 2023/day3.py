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

    edge cases:
        1. part number is at index 0 for line; can't look left
        2. part number is at last index for line; can't look right
        3. first line can't look up
        4. last line can't look down 
            
    """
    confirmed_part_nums = []
    sum = 0

    print(lines)

    for index, line in enumerate(lines):
        print(line)
        potential_part_nums = re.findall(r'\d+', line)
        confirmed_part_nums.append(potential_part_nums)

    print(confirmed_part_nums)
            
            
            
                
        

    


    
def part2(lines):
    pass

if __name__ == "__main__":
    main()