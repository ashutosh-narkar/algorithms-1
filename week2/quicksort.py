#!/usr/bin/env python
'''
Programming Assignment - 2
Compute the number of comparisons, given 10000 non-repeated integers.
Use quicksort to sort the integers.
'''
import os
import random
FILE_PATH = os.path.expanduser('~/coursera/algorithms1/week2/QuickSort.txt')
comparisons = 0


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


def partition(seq, left, right):
    '''
    Return the index of the pivot element
    '''
    pivot_index = _get_pivot_index(left, right)
    pivot_val = seq[pivot_index]
    store_index = left
    # move pivot element to rightmost end
    seq[right], seq[pivot_index] = seq[pivot_index], seq[right]

    for i in  range(left, right):
        if seq[i] < pivot_val:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1

    # pivot element compared with all other elements in the array
    global comparisons
    comparisons += len(seq) - 1

    # move the pivot element to correct position
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


def _get_pivot_index(left, right):
    '''
    Return the index of pivot element
    '''
    # Option 1 - Random selection:
    return random.randrange(left, right)

    # Option 2 - Leftmost element:
    #return left

    # Option 3 - Rightmost element:
    #return right

    # Option 4 - Middle element:
    #return (left + right) / 2


def quicksort(seq, left, right):
    '''
    Implement quicksort and counf number of comparions
    '''
    if len(seq) <= 1:
        return seq

    elif left < right:
        index = partition(seq, left, right)
        quicksort(seq, left, index - 1)
        quicksort(seq, index + 1, right)
        return seq


def main():
    '''
    Return the number of inversions
    '''
    data = read_data(FILE_PATH)
    res = quicksort(data, 0, len(data) - 1)
    print 'Number of comparisons {}'.format(comparisons)

if __name__ == '__main__':
    main()
