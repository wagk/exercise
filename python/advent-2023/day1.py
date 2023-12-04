import re

DATA = 'day1.data'
# DATA = 'day1-test.data'

NUMBERS = [
    ('one'  , '1'),
    ('two'  , '2'),
    ('three', '3'),
    ('four' , '4'),
    ('five' , '5'),
    ('six'  , '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine' , '9')
 ]

def replace_string_nums(s):
    ordering = [(idx, s.find(i))
                for (idx, (i, _))
                in enumerate(NUMBERS)]
    ordering = [(idx, i)
                for (idx, i)
                in ordering
                if i >= 0]

    # There are no word-numbers in this string
    if not ordering:
        return s

    min_idx = min(ordering, key = lambda x: x[1])[0]
    max_idx = max(ordering, key = lambda x: x[1])[0]
    s = s.replace(NUMBERS[min_idx][0], NUMBERS[min_idx][1])
    s = s.replace(NUMBERS[max_idx][0], NUMBERS[max_idx][1])
    return s

def find_digits(s):
    digits = [c for c in s if c.isdigit()]
    match digits:
        case [f, *_, l]:
            return (f, l)
        case [f]:
            return (f, None)
        case []:
            return (None, None)

with open(DATA, 'r') as data:
    total = 0
    for line in data:
        line.lower()
        line = replace_string_nums(line)
        match find_digits(line):
            case (None, None):
                continue
            case (num, None):
                total += int(num + num)
            case (first, last):
                total += int(first + last)

    print(f"{total = }")
