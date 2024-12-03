# Written by Josh Yeaton on 1/3/24
# For Advent of Code 2024

import re

f = open('data.txt')

total_pt1 = 0
total_pt2 = 0

full_line = ''

for l in f:
    full_line += l

mults = re.findall(r"mul\((\d+),(\d+)\)", full_line)
for mult in mults:
    total_pt1 += int(mult[0]) * int(mult[1])

# If last is a don't, we need to remove it. If it is a do, we don't
dos = re.finditer(r"do\(\)", full_line)
donts = re.finditer(r"don't\(\)", full_line)

last_do = 0
trimmed_l = full_line
for do in dos:
    last_do = do.start()

for dont in donts:
    dont_start = dont.start()
    if (dont_start > last_do):
        trimmed_l = trimmed_l[0:dont_start]

exclude_dont = re.sub(r"don't\(\).*?do\(\)", '', trimmed_l, flags=re.DOTALL)

mults_pt2 = re.findall(r"mul\((\d+),(\d+)\)", exclude_dont)
for mult in mults_pt2:
    total_pt2 += int(mult[0]) * int(mult[1])

        
print(total_pt1)
print(total_pt2)

f.close()