def gcd(a, b):                              # a, b both integers
    a, b = max(a, b), min(a, b)             # For first call, makes a the larger of the 2 values
    if (b == 0):
        return a
    return gcd(b, a % b)                    # Recursively call function until remainder is 0

# nuggets calculates the largest value that cannot be made by a list of values
# let x represent the smallest value in the list
# need to find the smallest number for which there exists x consecutive values that can be made
# then simply add x to these values to make the next x numbers, and so forth to create the remaining values
# need to find values that are congruent to y mod x for yE(1, x-1), values are denotated by y + n * x

def nuggets(a):                             # a is a list or tuple
    n = len(a)
    divisor = a[0]
    mod = min(a)                            # mod value is the smallest value in the list

    for i in range(n):
        divisor = gcd(divisor, a[i])
    
    if (divisor != 1):                      # gcd of the values determines whether or not a largest number exists
        return -1
    elif (mod == 1):                        # if smallest value is 1, all values can be made
        return 0
    
    mod_nums = [0 for x in range(mod)]      # mod_nums store the n value for each number that is congruent to y mod x represented by y + n * x at index y
    mod_table = []                          # mod_table store said y values for each n at index n

    for i in range(n):                      # loop goes through all coin values and stores the lowest n value for each y value, if no y value found, 0 is stored instead
        current  = a[i] % mod               
        multiple = int(a[i]/mod)            
        if (mod_nums[current] == 0):
            mod_nums[current] = multiple    
        else:
            mod_nums[current] = min(mod_nums[current], multiple)
    
    max_mod = max(mod_nums)                 # finds largest n value and appends n empty lists
    for i in range(max_mod + 1):
        mod_table.append([])
    
    for i in range(mod):                    # add y values for each n at index n
        mod_table[mod_nums[i]].append(i)
    
    mod_table[1].remove(0)                  # remove 0 mod x because x is congruent to 0 mod x

    # this while loop calculates new values that are congruent to y mod x represented by y + n * x, while minimizing n
    # all values for n = 1 have been found, search for n = 2 values
    # new y values obtained by (y1 + y2) % x, for y1, y2 values in n = 1, 
    # store new  y values for each n at index n, if index n does not exist, create by appending
    # remove y value from array index 0
    # increment count, or minimun n value
    # continue until no values are left in 0, or when all values of y have been found
    count = 2                               
    while (mod_table[0]):                   # 
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

    final = max(mod_table[max_mod]) + max_mod*mod - mod     # smallest value congruent to y mod x is given by y + max_mod * x
                                                            # largest unobtainable value is thus y + max_mod * x - x
    return final    

a = [3, 4, 17]
print(nuggets(a))