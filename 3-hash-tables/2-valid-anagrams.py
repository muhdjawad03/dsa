"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can
be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # O(n+m) solution to iterate through s and t
    char_dict_s = {}
    for char in s:
        char_dict_s[char] = char_dict_s.get(char, 0) + 1

    for char in t:
        # if char is new or if already the count in s is reached, it will be 0
        if char not in char_dict_s or char_dict_s[char] == 0:
            return False

        char_dict_s[char] -= 1

    # returns True if all of them are 0, else False
    return all(count == 0 for count in char_dict_s.values())


if __name__ == "__main__":
    str1 = "jam"
    str2 = "jar"
    print(is_anagram(str1, str2))
