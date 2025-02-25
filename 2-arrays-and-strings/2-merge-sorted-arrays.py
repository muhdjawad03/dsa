"""
Given 2 arrays that are sorted, merge them in a way that it is sorted as a whole

lst1 = [4, 5, 8, 10]
lst2 = [2, 5, 11, 58, 100]

Answer = [2, 4, 5, 5, 10, 11, 58, 100]
"""
import copy


# Bruteforce
def merge_sorted_arrays_bf(lst1: list, lst2: list) -> list:
    if not lst1 and not lst2:
        print("Both input lists are empty")
        return []

    if not lst1:
        return lst2  # lst2 is not empty and is already in sorted order
    if not lst2:
        return lst1  # lst1 is not empty and is already in sorted order

    merged_list = copy.copy(lst1)  # O(n)
    merged_list.extend(lst2)  # O(m)
    merged_list.sort()  # O((n+m) log (n+m)) as python uses time sort which has time complexity of n log n
    return merged_list


# Better solution with O(n+m)
def merge_sorted_arrays(lst1: list, lst2: list) -> list:
    if not lst1 and not lst2:
        print("Both input lists are empty")
        return []

    if not lst1:
        return lst2  # lst2 is not empty and is already in sorted order
    if not lst2:
        return lst1  # lst1 is not empty and is already in sorted order

    list1_length = len(lst1)
    list2_length = len(lst2)
    lp1, lp2 = 0, 0  # left_pointer1 for lst1 and left_pointer2 for lst2
    merged_array = []

    while lp1 < list1_length and lp2 < list2_length:
        if lst1[lp1] < lst2[lp2]:
            merged_array.append(lst1[lp1])
            lp1 += 1
        else:
            merged_array.append(lst2[lp2])
            lp2 += 1

    while lp1 < list1_length:
        merged_array.append(lst1[lp1])
        lp1 += 1

    while lp2 < list2_length:
        merged_array.append(lst2[lp2])
        lp2 += 1

    return merged_array  # O(n+m) as both arrays are traversed only once - no sorting explicitly

if __name__ == "__main__":
    input_arr1 = [4, 5, 8, 10]
    input_arr2 = [2, 5, 11, 58, 100]

    print(merge_sorted_arrays_bf(lst1=input_arr1, lst2=input_arr2))
    print(merge_sorted_arrays(lst1=input_arr1, lst2=input_arr2))