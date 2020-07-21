def linear_search(arr, target):
    # Your code here
    # loop through the array
    for i in range(len(arr)):
        # check if index matches target and return it
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    middle = 0
    high = len(arr) - 1

    while low <= high:
        # get middle of the array
        middle = (high + low) // 2
        # if middle index is less than target, reassign low to above middle
        if arr[middle] < target:
            low = middle + 1
        # if middle index is more than target, reassign high to below middle
        elif arr[middle] > target:
            high = middle - 1
        # return middle if target matches
        else:
            return middle
    return -1  # not found
