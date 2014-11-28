#!/usr/bin/env python
'''
Implement the Randomized Selection Algorithm
Given a list of unsorted integers, return the ith order statistic
(ie. ith smallest element in the list)
eg Find 2nd order statistic in [3,1,4,2]
Answer -> 2

Average Runtime O(n)
'''
import random


def partition(seq):
    '''
    Return the index of the pivot element
    '''
    right = len(seq) - 1
    left = 0
    pivot_index = random.randrange(left, right)
    pivot_val = seq[pivot_index]
    store_index = left

    # move pivot element to rightmost end
    seq[right], seq[pivot_index] = seq[pivot_index], seq[right]

    for i in range(left, right):
        if seq[i] < pivot_val:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1

    # move the pivot element to correct position
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


def rselect(seq, order):
    '''
    Find the ith order statistic
    '''
    if not seq:
        return -1

    if len(seq) == 1:
        return seq[0]

    index = partition(seq)

    # Since we are using zero-indexed list
    if index == order - 1:
        return seq[index]

    # ith order statistic is to the left of pivot
    elif order <= index:
        return rselect(seq[:index], order)

    # ith order statistic is to the right of pivot
    else:
        return rselect(seq[index + 1:], order - index - 1)


def main():
    '''
    Return the number of inversions
    '''
    data = [12, 14, 111, 0, -3, -2]
    order = 3
    # ith order statistic will be the element at
    # position i - 1 in the list
    res = rselect(data, order)
    print 'Input: {} Order: {} Result: {}'.format(data, order, res)

if __name__ == '__main__':
    main()
