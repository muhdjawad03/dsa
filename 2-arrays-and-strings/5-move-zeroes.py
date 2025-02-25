"""
Given integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def move_zeroes(nums: list) -> list:
    lp = 0

    # O(n) time complexity as iterating only once
    for rp in range(len(nums)):
        if nums[rp] != 0:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1  # This will track the place where to swap the non-zero element next time

    return nums


if __name__ == "__main__":
    input_lst = [1,0,1,0,3,12]
    print(move_zeroes(input_lst))