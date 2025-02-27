"""
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return None

"""

def first_recurring_char(input_arr: list) -> int | None:
    if not input_arr:
        return None

    my_set = set()
    # O(n) solution as in the worst case, it will iterate whole input_arr
    for item in input_arr:
        if item in my_set:
            return item
        my_set.add(item)

    return None

if __name__ == "__main__":
    arr = [2,5,1,2,3,5,1,2,4]
    print(first_recurring_char(arr))