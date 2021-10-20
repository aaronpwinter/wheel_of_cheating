import os
import re
from collections import defaultdict

'''
Turns "___A ____" (3underscores, A, space, 4 underscores) into a regex
        "^\w{3}[A]\s\w{4}$"
'''
REGEX_START = r'\b'#'^'
REGEX_END = r'\b'#'$'
ALL_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def regex_please(s: str, guessed_letters: str = '') -> str:
    s = s.upper().strip()
    search_letters = ALL_LETTERS
    for i in guessed_letters:
        search_letters = re.sub(i, '', search_letters)

    returning = REGEX_START

    blank_spaces = 0

    for char in s:
        if 'A' <= char <= 'Z' or char in '-&':
            if blank_spaces > 0:
                returning += '[' + search_letters + ']{' + f'{blank_spaces}' + '}'
                blank_spaces = 0
            returning += f'{char}'
        elif char == ' ':
            if blank_spaces > 0:
                returning += '[' + search_letters + ']{' + f'{blank_spaces}' + '}'
                blank_spaces = 0
            returning += '\s'
        elif char in '_.,/;\'\\=':
            blank_spaces += 1

    
    if blank_spaces > 0:
        returning += '[' + search_letters + ']{' + f'{blank_spaces}' + '}'
        blank_spaces = 0

    returning += REGEX_END
    return returning

'''
Removes symbols
'''
SYMBOLS = ':|\'|"|\-|_|\.|!|\\|\?|&'
def remove_symbols(s: str) -> str:
    s = s.upper()
    return re.sub(SYMBOLS, '', s).strip()


'''
Removes 'The ' from beginning
'''
def remove_the(s: str) -> str:
    s = s.upper()
    return s.lstrip('THE').strip()

'''
Removes the wikipedia "[wafdsa]"
'''
def remove_citation(s: str) -> str:
    return re.sub(r'\[\w*\]', '', s.upper())

'''
Does the above
'''
def clean(s: str) -> str:
    return remove_citation(remove_the(remove_symbols(s)))

if __name__ == '__main__':
    
    guess = input()
    while guess != '':
        guessed = input().upper()
        re_string = regex_please(guess, guessed)
        print(re_string)

        matching_games = set()
        the_file = open('listOfItems.txt', 'r')

        for line in the_file:
            line = line.strip().rstrip('\n').upper()
            if adder := re.search(re_string, line):
                matching_games.add(adder.group(0))
            if remove_symbols(line) != line and (adder := re.search(re_string, remove_symbols(line))):
                matching_games.add(adder.group(0))
            if clean(line) != line and (adder := re.search(re_string, clean(line))):
                matching_games.add(adder.group(0))

        
        letters = defaultdict(lambda: 0)
        for i in sorted(matching_games):
            print(i)
            for char in i:
                if char != ' ':
                    letters[char] += 1

        sorted_letters = sorted(letters.items(), key = lambda x: -x[1])
        for l in sorted_letters:
            print(l[0], ':', l[1])

        the_file.close()
        guess = input()
