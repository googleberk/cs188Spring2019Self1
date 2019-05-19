import random
import time

random.seed(3340)
test = random.sample(range(10000000), 10000)
print(test)


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
        while l <= g and a[l] < pivot:
            l += 1
        while g >= l and a[g] > pivot:
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
    print(test)
    print("--- %s seconds ---" % (end_time3 - start_time3))
