import re

DATA = 'day1.data'
# DATA = 'day1-test.data'

NUMS = {
    'zero' : '0',
    'one'  : '1',
    'two'  : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9',
    '1'    : '1',
    '2'    : '2',
    '3'    : '3',
    '4'    : '4',
    '5'    : '5',
    '6'    : '6',
    '7'    : '7',
    '8'    : '8',
    '9'    : '9',
}

def find_numbers(s):
    r = r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))'
    num_list = [NUMS[n] for n in re.findall(r, s)]
    return (num_list[0], num_list[-1])

with open(DATA, 'r') as data:
    total = 0
    for line in data:
        line.lower()
        (min, max) = find_numbers(line)
        total += int(min + max)

    print(f"{total = }")
