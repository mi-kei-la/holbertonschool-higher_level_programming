#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        romans = {'M': 1000, 'D': 500, 'C': 100}
        l = {'L': 50, 'X': 10, 'V': 5, 'I': 1}
        romans.update(l)
        nums = list(map(lambda x: romans.get(x), roman_string))
        for i in roman_string:
            if i not in romans:
                return None
        count = len(nums)
        total = 0
        l = count
        c = count - 1
        for i in range(0, count):
            l = i + 1
            if i in range(0, count - 1):
                if nums[i] < nums[l]:
                    total = total - nums[i]
                else:
                    total = total + nums[i]
        total = total + nums[c]
        return total
    else:
        return None
