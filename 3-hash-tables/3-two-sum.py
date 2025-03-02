"""
Given array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

def two_sum(input_arr: list, target: int) -> list:
    if not input_arr:
        print("Empty input array")
        return []

    seen_indices = {}

    # O(n) because we only iterate once
    for i, num in enumerate(input_arr):
        difference = target - num

        if difference in seen_indices:  # if the value exists in seen_indices, found a match
            return [seen_indices[difference], i]

        seen_indices[num] = i

    return []  # in case of no matches


if __name__ == "__main__":
    nums = [3,3]
    target_val = 6
    print(two_sum(input_arr=nums, target=target_val))