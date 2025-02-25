"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

def rotate_array(input_arr: list, rotations: int) -> list:
    if not input_arr:
        print("Empty input array")
        return []

    if rotations == 0:
        return input_arr

    # O(n) time and space complexity
    rotations %= len(input_arr)
    return input_arr[-rotations:] + input_arr[:-rotations]

if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7]
    # k = 3
    arr = [-1,-100,3,99]
    k = 2
    print(rotate_array(arr, k))
