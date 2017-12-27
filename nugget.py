def nuggets(a, n):
    divisor = a[0]
    mod = INF
    for i in range(n):
        divisor = gcd(divisor, a[i])
        if (a[i] < mod):
            mod = a[i]
    
    if (divisor != 1):
        return -1
    
    mod_nums = [0 for x in range(mod)]
    
    mod_table = []

    for i in range(n):
        current  = a[i] % mod
        multiple = int(a[i]/mod)
        if (mod_nums[current] = 0):
            mod_nums[current] = muliple
        else:
            mod_nums[current] = min(mod_nums[current], multiple)
    
    temp = max(mod_nums)
    for i in range(temp):
        mod_table.append([])
    
    for i in range(mod):
        mod_table[mon_nums[i]].append(i)

    count = 2
    while (not mod_table[0]):
        for i in range(1, int(count/2)):
            


    

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if (b == 0):
        return a
    return gcd(b, a % b)
        