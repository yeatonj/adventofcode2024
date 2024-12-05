# Written by Josh Yeaton on 1/5/24
# For Advent of Code 2024

def check_score(t, rules):
    violation = False
    for i in range(len(t) - 1):
        for j in range(i + 1, len(t)):
            if ((t[j] in rules) and (t[i] in rules.get(t[j]))):
                violation = True
                to_reorder.append(t)
                break
        if violation:
            break
    if (not violation):
        return t[len(t) // 2]
    else:
        return 0
    
def reorder_pages(t, rules):
    sorted = []
    for val in t:
        if (val not in rules):
            sorted.append(val)
            continue
        if (len(sorted) == 0):
            sorted.append(val)
            continue
        inserted = False
        for i in range(len(sorted)):
            compare_val = sorted[i]
            if (compare_val in rules.get(val)):
                sorted.insert(i, val)
                inserted = True
                break
        if (not inserted):
            sorted.append(val)
    return sorted[len(sorted) // 2]
        


if __name__ == "__main__":
    f = open('data.txt')

    rules = {}

    tests = []

    for l in f:
        l = l.strip()
        if ('|' in l):
            num_arr = l.split('|')
            source = int(num_arr[0])
            dest = int(num_arr[1])
            if source not in rules:
                rules.update({source:{}})
            rules.get(source).update({dest:1})
        elif (',' in l):
            to_visit = l.split(',')
            test = [int(i) for i in to_visit]
            tests.append(test)

    f.close()

    total_pt1 = 0
    to_reorder = []
    # Data loaded, attempt to step thru
    for t in tests:
        total_pt1 += check_score(t, rules)


    print(total_pt1)
    total_pt2 = 0
    # print(to_reorder)
    for t in to_reorder:
        total_pt2 += reorder_pages(t, rules)
    print(total_pt2)
    # 9630 is too high (passing too many)


    