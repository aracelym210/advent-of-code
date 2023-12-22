"""
    author: aracelym
    date: 12/13/2023
    problem: https://adventofcode.com/2023/day/2
    
"""
import re
def main():
    games = []
    with open('inputs/day2.txt', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        games.append(line.strip())
    
    #part1(games)
    part2(games)

def part1(games):
    game_pieces = {'blue': 14, 'green': 13, 'red': 12}
    valid_games = []
    for game in games:
        game_id = game.split(':')[0].strip()
        turns = game.split(':')[1].strip()
        rolls = turns.split(';')

        for roll in rolls:
            if 'red' in roll:
                match = re.findall(r'(\d+).red', roll)
                if int(match[0]) <= game_pieces['red']:
                    red_valid = True
                else:
                    red_valid = False
                    break
            if 'blue' in roll:
                match = re.findall(r'(\d+).blue', roll)
                if int(match[0]) <= game_pieces['blue']:
                    blue_valid = True
                else:
                    blue_valid = False
                    break
            if 'green' in roll:
                match = re.findall(r'(\d+).green', roll)
                if int(match[0]) <= game_pieces['green']:
                    green_valid = True
                else:
                    green_valid = False
                    break
            
        if red_valid and blue_valid and green_valid:
            valid_games.append(game_id) 

    sum = 0
    for game in valid_games:
        match = re.findall(r'\d+', game)
        sum += int(match[0])      
    print(sum)
        
def part2(games):
    powers = []
    sum = 0

    # uses map() function to make sure list of ints is created; not list of str
    for game in games:
        if 'red' in game:
            reds = list(map(int,re.findall(r'(\d+).red', game)))
        if 'blue' in game:
            blues = list(map(int, re.findall(r'(\d+).blue', game)))
        if 'green' in game:
            greens = list(map(int, re.findall(r'(\d+).green', game)))
        
        max_red = max(reds)
        max_blue = max(blues)
        max_green = max(greens)
        powers.append(max_red * max_blue * max_green)
    
    for power in powers:
        sum += power

    print(sum)
    

if __name__ == '__main__':
    main()