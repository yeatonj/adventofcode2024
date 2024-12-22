# Written by Josh Yeaton on 1/22/24
# For Advent of Code 2024

def mix(secret, mix_num):
    return secret ^ mix_num

def prune(secret):
    return secret % 16777216

def find_secret(secret, iter):
    for i in range(iter):
        # step 1
        temp = secret
        temp *= 64
        secret = mix(secret, temp)
        secret = prune(secret)
        # Step 2
        temp = secret
        temp //= 32
        secret = mix(secret,temp)
        secret = prune(secret)
        # Step 3
        temp = secret
        temp *= 2048
        secret = mix(secret,temp)
        secret = prune(secret)
    return secret


if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)

    nums = []
    for l in f:
        l = l.strip()
        nums.append(int(l))
    f.close()

    total = 0
    
    all_prices = []
    prices_and_changes = []

    for n in nums:
        temp_price = []
        secret_num = n
        temp_price.append(secret_num % 10)
        for i in range(2000):
            secret_num = find_secret(secret_num, 1)
            temp_price.append(secret_num % 10)
        total += secret_num
        all_prices.append(temp_price)
        temp_price_change = []
        for i in range(1, len(temp_price)):
            change = temp_price[i] - temp_price[i - 1]
            combined = (temp_price[i], change)
            temp_price_change.append(combined)
        prices_and_changes.append(temp_price_change)
    print(total)

    # now do part 2
    seq_dic_arr = []
    for i in range(len(prices_and_changes)):
        temp_dic = {}
        cur_seq = prices_and_changes[i]
        for j in range(3, len(cur_seq)):
            change_seq = (cur_seq[j - 3][1], cur_seq[j - 2][1], cur_seq[j - 1][1], cur_seq[j][1])
            if (temp_dic.get(change_seq) == None):
                temp_dic.update({change_seq:cur_seq[j][0]})


        seq_dic_arr.append(temp_dic)

    # print(seq_dic_arr)

    checked = {}
    max = 0
    for i in range(len(seq_dic_arr)):
        for seq in seq_dic_arr[i]:
            if (checked.get(seq) != None):
                continue
            subtotal = seq_dic_arr[i].get(seq)
            for j in range(i + 1, len(seq_dic_arr)):
                if (seq_dic_arr[j].get(seq) != None):
                    subtotal += seq_dic_arr[j].get(seq)
            checked.update({seq:subtotal})
            if (subtotal > max):
                max = subtotal
                max_seq = seq
    print(max)
            
            