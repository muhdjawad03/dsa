"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

def largest_sub_array_sum(input_lst: list) -> int:
    if not input_lst:
        return 0

    curr_sum = 0
    max_value = input_lst[0]

    # O(n) solution
    for num in input_lst:
        if curr_sum < 0:
            curr_sum = 0

        curr_sum += num
        max_value = max(max_value, curr_sum)

    return max_value

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(largest_sub_array_sum(nums))