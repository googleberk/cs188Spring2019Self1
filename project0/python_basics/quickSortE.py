import random
import time

# Quicksort is a divide and conquer algorithm.
# Quicksort first divides a large array into two smaller sub-arrays:
# the low elements and the high elements. Quicksort can then recursively sort the sub-arrays. The steps are:
#
# Pick an element, called a pivot, from the array.
# Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot,
# while all elements with values greater than the pivot come after it (equal values can go either way).
# After this partitioning, the pivot is in its final position. This is called the partition operation.

# Recursively apply the above steps to the sub-array of elements with smaller values and separately
# to the sub-array of elements with greater values.
# The base case of the recursion is arrays of size zero or one, which are in order by definition,
# so they never need to be sorted.
#
# The pivot selection and partitioning steps can be done in several different ways;
# the choice of specific implementation schemes greatly affects the algorithm's performance.

a = [17, 15, 19, 32, 2, 26, 41, 17, 17]

random.seed(305)
test = random.sample(range(10000000), 1000000)


def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    list_small = [x for x in a[1:] if x < pivot]
    list_big = [x for x in a[1:] if x >= pivot]
    return quicksort(list_small) + [pivot] + quicksort(list_big)


# Main Function
if __name__ == '__main__':
    start_time1 = time.time()
    # b = quicksort(a)
    c = quicksort(test)
    end_time1 = time.time()
    # print(c)
    print("Three Scan Quick Sort that sorts 1000000 numbers takes: " + "--- %s seconds ---" % (end_time1 - start_time1))
    # print(b)

# Note1: above code is an Algorithm in CS61B called Leftmost-Three-Scan QuickSort:
# which means that this algorithm uses the left most position of an array as the pivot position
# and then scan the entire list three times to get the smaller items, itself, and the bigger items
# ,which corresponds to the list comprehension process above

# Note2: below is the Lomuto partition scheme from WiKi:
# pseudocode is below:
# algorithm quicksort(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort(A, lo, p - 1)
#         quicksort(A, p + 1, hi)
#
# algorithm partition(A, lo, hi) is
#     pivot := A[hi]
#     i := lo
#     for j := lo to hi - 1 do
#         if A[j] < pivot then
#             swap A[i] with A[j]
#             i := i + 1
#     swap A[i] with A[hi]
#     return i

random.seed(305)
test = random.sample(range(10000000), 1000000)


def quickSortLomuto(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quickSortLomuto(a, lo, p - 1)
        quickSortLomuto(a, p + 1, hi)


def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            swap(a, i, j)
            i += 1
    swap(a, i, hi)
    return i


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Main Function
if __name__ == '__main__':
    start_time2 = time.time()
    # quickSortLomuto(a, 0, len(a) - 1)
    quickSortLomuto(test, 0, len(test) - 1)
    end_time2 = time.time()
    # print(test)
    print("Lomuto partition Quick Sort that sorts 1000000 numbers takes: " + "--- %s seconds ---" % (
            end_time2 - start_time2))
    # print(a)

# Note3: below is the implementation for another type of QuickSort:
# Tony Hoare partition scheme from CS61B Spring2019 lecture32
"Bad Note: the pseudocode from WiKi is not working: haven't look through it yet!"

# Algorithm:
# : create L and G pointers at a[1] and a[len(a)-1]
#        L pointer is a friend to small items, and hates large or equal items.
#        G pointer is a friend to large items, and hates small or equal items.
# : Walk pointers towards each other, stopping on a hatred item
#        When both pointers have stopped, swap and move pointers bt one
#        When pointers cross, you are done walking.
# : Swap pivot with G

random.seed(305)
test = random.sample(range(10000000), 1000000)


def quickSortHoare(a, lo, hi):
    if lo < hi:
        old_pivot = partition2(a, lo, hi)
        quickSortHoare(a, lo, old_pivot - 1)
        quickSortHoare(a, old_pivot + 1, hi)


def partition2(a, lo, hi):
    pivot = a[lo]
    l = lo + 1
    g = hi
    while True:
        while a[l] < pivot:
            l += 1
        while a[g] > pivot:
            g -= 1
        if l > g:
            break
        swap2(a, l, g)
        l += 1
        g -= 1
    swap2(a, lo, g)
    return g


def swap2(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Main Function
if __name__ == '__main__':
    start_time3 = time.time()
    quickSortHoare(test, 0, len(test) - 1)
    end_time3 = time.time()
    # print(test)
    print("Tony Hoare partition Quick Sort that sorts 1000000 numbers takes: " + "--- %s seconds ---" % (
            end_time3 - start_time3))
