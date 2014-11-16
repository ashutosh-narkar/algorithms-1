#!/usr/bin/env python
'''
Programming Assignment - 6 Q2
Implement the "Median Maintenance" algorithm.

Input is list of the integers from 1 to 10000
in unsorted order arriving one at a time
Compute the median when a new number arrives.
Finally compute (m1+m2+m3+..+m10000)mod10000

Running time - O(log i), where i number of integers at step 'i'
'''
from heapq import heappush, heappop
import os
INPUT_FILE = os.path.expanduser('~/coursera/algorithms1/week6/Median.txt')


def read_input():
    '''
    Read the input file containg integers from 1 to 10000
    '''
    numbers = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            val = int(line.strip())
            numbers.append(val)
    return numbers


def median_maintain(inputs):
    '''
    Given the list of numbers, maintain
    the median at any given time

    To maintain a max-heap in Python, we invert the value of
    the number and then use the heapq api
    '''
    heap_low = []   # max-heap
    heap_high = []  # min-heap

    # insert first 2 numbers in any of the heaps
    heappush(heap_high, inputs[0])
    heappush(heap_low, -inputs[1])

    # maintain a list of medians at every step
    medians = []
    medians.append(inputs[0])  # since only one item
    medians.append(_calculate_new_median(heap_low, heap_high))

    for num in inputs[2:]:
        if num <= -heap_low[0]:
            heappush(heap_low, -num)
        else:
            heappush(heap_high, num)
        _ckeck_if_rebalancing_needed(heap_low, heap_high)
        new_median = _calculate_new_median(heap_low, heap_high)
        medians.append(new_median)
    return medians


def _calculate_new_median(heap_low, heap_high):
    '''
    Given 2 heaps, return the median among them
    '''
    if len(heap_low) == len(heap_high):
        return(min(-heap_low[0], heap_high[0]))

    elif len(heap_low) > len(heap_high):
        return -heap_low[0]

    else:
        return heap_high[0]


def _ckeck_if_rebalancing_needed(heap_low, heap_high):
    '''
    Given 2 heaps check if they need to be rebalanced
    abs(len(h1) - len(h2)) <= 1 means heaps are balanced
    '''
    if abs(len(heap_low) - len(heap_high)) <= 1:
        return

    if len(heap_low) > len(heap_high):
        val = -heappop(heap_low)  # negate since we
                                  # inserted items with negation
        heappush(heap_high, val)

    else:
        val = heappop(heap_high)
        heappush(heap_low, -val)  # negate since we maintain a max-heap


def main():
    '''
    Calculate Median Maintenance
    '''
    input_numbers = read_input()
    medians = median_maintain(input_numbers)
    print sum(medians) % 10000

if __name__ == '__main__':
    main()
