def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1


# Write an iterative implementation of Binary Search
# iterate over sorted array to find specific value
# start at midpoint of array
# do comparison to value
# if value is higher than target value go right
# if value is lower than target value go left
# midpoint will eventually by equal to target value or
# value will have no more values to its left or right to compare
# when target value is found stop the algorithm and return the value

def binary_search(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint

        elif target < midpoint_value:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return -1
