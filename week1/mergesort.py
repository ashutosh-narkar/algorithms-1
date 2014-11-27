#!/usr/bin/env python
'''
Programming Assignment - 1
Compute the number of inversions, given 100000 non-repeated integers.
Use mergesort to sort the integers
'''
import os
FILE_PATH = os.path.expanduser('~/coursera/algorithms1/week1/IntegerArray.txt')
inversions = 0


def read_data(path):
    '''
    Read the file data containing the integers
    '''
    numbers = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            numbers.append(int(line))
    return numbers


def merge(left, right):
    '''
    Implement merge step of mergesort
    '''
    result = []
    n, m = 0, 0

    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1
            global inversions
            inversions += len(left[n:])

    result.extend(left[n:])
    result.extend(right[m:])
    return result


def sort(seq):
    '''
    Implement divide step of mergesort
    '''
    if len(seq) <= 1:
        return seq

    middle = len(seq) / 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)


def main():
    '''
    Return the number of inversions
    '''
    data = read_data(FILE_PATH)
    result = sort(data)
    print 'Number of inversions {}'.format(inversions)


if __name__ == '__main__':
    main()
