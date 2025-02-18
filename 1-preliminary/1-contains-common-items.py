"""
Given 2 arrays, create a function to let user know whether two arrays contain any common items

Ex1:
array_1 = ['a', 'b', 'c', 'x']
array_2 = ['p', 'u', 'y']
should return False

Ex2:
array_1 = ['a', 'b', 'c', 'x']
array_2 = ['x', 'h', 'j']
should return True

"""


# Brute-force : O(n*m)
def contains_common_bf(arr1: list[any], arr2: list[any]) -> bool:
    if not any([arr1, arr2]):  # O(1) constant time as any checks only first element
        return False

    # Time complexity will be O(n*m) because of look up in list is linear time
    for item in arr1:
        if item in arr2:
            return True  # Found item

    return False


# Better solution : O(n+m) - because conversion from list to set is O(n). Using set will be efficient here.
def contains_common(arr1: list[any], arr2: list[any]) -> bool:
    return bool(set(arr1) & set(arr2))


if __name__ == "__main__":
    array_1 = ['a', 'b', 'c', 'x']
    array_2 = ['x', 'h', 'j']
    print(contains_common_bf(arr1=array_1, arr2=array_2))
    print(contains_common(arr1=array_1, arr2=array_2))
