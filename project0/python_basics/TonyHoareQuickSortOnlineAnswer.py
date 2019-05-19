import random
# quick sort
random.seed(305)
test = random.sample(range(1000000), 10000)

def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
    # swap start with myList[right]
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split - 1)
        quicksort(myList, split + 1, end)
    return myList


if __name__ == "__main__":
    sortedList = quicksort(test, 0, len(test) - 1)
    print(sortedList)
