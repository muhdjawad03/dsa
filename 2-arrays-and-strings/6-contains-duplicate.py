"""
Given integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def contains_duplicate(nums: list) -> bool:
    if not nums:
        print("Input list is empty")
        return False

    # O(n) time and space complexity
    return not len(nums) == len(set(nums))


def contains_duplicate_iteration(nums: list) -> bool:
    seen = set()  # Not creating entire set(list)initially - better in terms of space for non worst case scenario

    for num in nums:
        if num in seen:
            return True  # Early exit for non worst case
        seen.add(num)

    return False


if __name__ == "__main__":
    input_lst = [1,2,3,4]
    print(contains_duplicate(input_lst))
    print(contains_duplicate_iteration(input_lst))