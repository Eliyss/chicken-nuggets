def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if (b == 0):
        return a
    return gcd(b, a % b)
        
def nuggets(a):
    n = len(a)
    divisor = a[0]
    mod = min(a)

    for i in range(n):
        divisor = gcd(divisor, a[i])
    
    if (divisor != 1):
        return -1
    elif (mod == 1):
        return 0
    
    mod_nums = [0 for x in range(mod)]
    
    mod_table = []

    for i in range(n):
        current  = a[i] % mod
        multiple = int(a[i]/mod)
        if (mod_nums[current] == 0):
            mod_nums[current] = multiple
        else:
            mod_nums[current] = min(mod_nums[current], multiple)
    
    max_mod = max(mod_nums)
    for i in range(max_mod + 1):
        mod_table.append([])
    
    for i in range(mod):
        mod_table[mod_nums[i]].append(i)
    
    mod_table[1].remove(0)

    print(mod_table[1])
    count = 2
    while (mod_table[0]):
        for i in range(1, int(count/2) + 1):
            for j in range(len(mod_table[i])):
                for k in range(len(mod_table[count-i])):
                    new_nugget = mod_table[i][j] + mod_table[count-i][k]
                    over_mod = int(new_nugget/mod)
                    new_nugget = new_nugget % mod
                    if (new_nugget in mod_table[0]):
                        while (max_mod < count + over_mod):
                            mod_table.append([])
                            max_mod += 1
                        mod_table[count + over_mod].append(new_nugget)
                        mod_table[0].remove(new_nugget)
        count += 1

    final = max(mod_table[max_mod]) + max_mod*mod - mod
    return final    

a = [11, 13, 17]
print(nuggets(a))