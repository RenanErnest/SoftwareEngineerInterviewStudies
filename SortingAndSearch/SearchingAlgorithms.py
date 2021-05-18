'''
Time complexity: O(logn) where n is the number of elements
Space complexity: O(1)
'''
def binary_search(lst, val):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low + (high-low)//2
        if val > lst[mid]:
            low = mid + 1
        elif val < lst[mid]:
            high = mid - 1
        else:
            return True
    return False


'''
Time complexity: O(logn) where n is the number of elements in the list
Space complexity: O(logn) because of the recursive calls
'''
def binary_search_recursive(lst, val):
    return binary_search_recursive_helper(lst, 0, len(lst)-1, val)


def binary_search_recursive_helper(lst, low, high, val):
    if low > high:
        return False
    mid = (low + high) // 2  # can also be mid = low + (high-low)//2
    if val > lst[mid]:
        return binary_search_recursive_helper(lst, mid+1, high, val)
    elif val < lst[mid]:
        return binary_search_recursive_helper(lst, low, mid-1, val)
    else:
        return True


print(binary_search([1, 4, 5, 6, 7, 8], 5))
print(binary_search([1, 4, 5, 6, 7, 8], 10))
print(binary_search_recursive([1, 4, 5, 6, 7, 8], 5))
print(binary_search_recursive([1, 4, 5, 6, 7, 8], 10))