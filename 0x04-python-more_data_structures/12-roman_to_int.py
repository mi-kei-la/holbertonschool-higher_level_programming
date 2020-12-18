#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string != None:
        romans = {'M' : 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        nums = list(map(lambda x: romans.get(x), roman_string))
        count = len(nums)
        total = 0
        l = 1
        for i in range(count, 0, -1):
            print("this is i: {}" .format(i))
            while (count > l):
                if (i < nums[l]):
                    total = total - i
                else:
                    total = total + i
                l = l + 1
                print("this is total on {} iteration: {}" .format(i, total))
        l = len(nums)
        total = total + nums[l - 1] 
        return total
