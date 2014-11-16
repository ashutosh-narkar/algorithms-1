#!/usr/bin/env python
'''
Programming Assignment - 6 Q1
Implement the 2-SUM algorithm.

Input is 1 million integers,
both positive and negative (there might be some repetitions!)
Compute the number of target values t
in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,y in
the input that satisfy x+y=t
'''
import os
INPUT_FILE = os.path.expanduser('~/coursera/algorithms1/week6/'
                                'algo1-programming_prob-2sum.txt')


def create_dict():
    '''
    Read the input file containg 1 million
    integers and store them in a dict keyed on the integer
    and value is their occurence count
    '''
    numbers = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            val = int(line.strip())
            numbers.append(val)
    return numbers


def calculate_two_sum(numbers):
    '''
    Given a dict keyed on numbers and their occurence count,
    compute the number of target values t in the
    interval [-10000,10000] (inclusive),
    such that there are distinct numbers x,y in
    the input that satisfy x+y=t

    Idea: Since -10000 <= x + y <= 10000, hence -10000 -x <= y <= 10000 - x
    '''

    result = 0
    numbers.sort()
    two_sum = set()

    for number in numbers:
        low = -10000 - number
        high = 10000 - number

        # Solution 1: for every value in (low, high)(inclusive),
        # check if the value, is in the given numbers
        # if present, increment result by 1, if the sum of the value and
        # x(current iteration number),
        # is currently not present in the set two_sum

        # Solution 2: Better and faster solution
        # Instead of iterating through every single value in range (low, high),
        # find the index of the numbers closest to
        # 'low' and 'high' in the sorted numbers list.
        # Now we only iterate over a small slice of the
        # sorted numbers list instead of iterating
        # over 20001 values for each of the million
        # Running Time: O(nlogn)

        new_high = _find_closest(numbers, high)
        new_low = _find_closest(numbers, low)

        for i in numbers[new_low:new_high + 1]:
            if i != number:
                _sum = i + number
                if -10000 <= _sum <= 10000 and _sum not in two_sum:
                    two_sum.add(_sum)
                    result += 1

    return result


def _find_closest(numbers, val):
    '''
    Use binary search to find a number
    in 'numbers' closest to 'val'
    and return its index
    '''
    low = 0
    high = len(numbers) - 1

    while (low <= high):
        mid = (low + high) / 2
        if numbers[mid] == val:
            return mid
        elif val > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    try:
        numbers[low]
    except IndexError, e:
        return high
    else:
        return low


def main():
    '''
    Calculate 2-SUM
    '''
    input_numbers = create_dict()
    print calculate_two_sum(input_numbers)

if __name__ == '__main__':
    main()
