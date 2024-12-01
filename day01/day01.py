# Written by Josh Yeaton on 1/1/24
# For Advent of Code 2024

f = open("data.txt")

left = []
right = []

for l in f:
    l = l.strip()
    split_l = l.split()
    left.append(int(split_l[0]))
    right.append(int(split_l[1]))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += abs(left[i] - right[i])

print("Solution to part 1 is {}.".format(total))

# Add to sim dic
sim_dic = {}
for val in right:
    if val in sim_dic:
        cur = sim_dic.get(val)
        sim_dic.update({val:cur + 1})
    else:
        sim_dic.update({val:1})

sim_score = 0
for val in left:
    if val in sim_dic:
        sim_score += val * sim_dic.get(val)

print("Solution to part 2 is {}.".format(sim_score))

f.close()
