"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverse_a_string_loop(input_array: list[str]) -> list:
    if not input_array:
        print("Empty array")
        return []

    i, j = 0, len(input_array)-1
    while i < j:
        input_array[i], input_array[j] = input_array[j], input_array[i]
        i += 1
        j -= 1

    return input_array

def reverse_a_string(input_array: list[str]) -> list:
    if not input_array:
        print("Empty input array")
        return []

    # For O(1) space we need to use slicing bcs input_array creates a new list without slicing, which is O(n)
    input_array[:] = input_array[::-1]
    return input_array


if __name__ == "__main__":
    input_lst = ["d", "a", "w", "a", "j"]
    print(reverse_a_string(input_array=input_lst))

    input_lst_2 = ["o","l","l","e","h"]
    print(reverse_a_string_loop(input_array=input_lst_2))
