def remove_even(lst):
    i = 0  # index handling the storage of odd numbers
    for num in lst:
        if num % 2 != 0:
            lst[i] = num
            i += 1
    return lst[:i]


# [1,3,5] [2,4]
def merge_lists(lst1, lst2):
    merged = []
    i = 0  # index for lst1
    j = 0  # index for lst2

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    if i < len(lst1):  # O(n) in worst case where n = size(lst1)
        merged.extend(lst1[i:])
    if j < len(lst2):  # O(m) in worts case where m = size(lst2)
        merged.extend(lst2[j:])

    return merged


def find_sum(lst, k):
    complement_map = {}  # {80:1, 60:21, 78:3, 67:14, 76:5, }
    for num in lst:
        if num in complement_map:
            return [num, complement_map[num]]
        complement = k - num
        complement_map[complement] = num
    return None


def find_product(lst):  # not most optimal, approach with the left and right array, must be reviewed
    product = 1
    for num in lst:
        product *= num

    for i in range(len(lst)):
        lst[i] = product / lst[i]

    return lst


def find_minimum(arr):
    minimum = float('Inf')
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum


def find_first_unique(lst):
    occurrences = {num: 0 for num in lst}  # 2:2 3:1 6:2 9:1
    for num in lst:
        occurrences[num] += 1

    for num in lst:
        if occurrences[num] == 1:
            return num

    return None


def find_second_maximum(lst):
    if len(lst) < 2:
        return None

    maximum = -float('Inf')
    second_maximum = -float('Inf')
    for num in lst:
        if num > maximum:
            second_maximum = maximum
            maximum = num
        elif num > second_maximum:
            second_maximum = num

    return second_maximum


def right_rotate(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    k = len(lst) - k
    left = lst[:k]
    right = lst[k:]
    return right + left


'''
[-1,-9,-6,4,5,10,20]
        i         j
'''
def rearrange(lst):
    i = 0  # pointer of negative numbers
    j = 0  # pointer to iterate over the list
    while j < len(lst):
        if lst[j] < 0:
            # swap lst[j] with lst[i]
            aux = lst[i]
            lst[i] = lst[j]
            lst[j] = aux
            i += 1
        j += 1

    return lst


def max_min(lst):
    max_min_lst = []
    left = 0
    right = len(lst) - 1

    while left <= right:
        max_min_lst.append(lst[right])
        right -= 1
        if left <= right:
            max_min_lst.append(lst[left])
            left += 1

    return max_min_lst


def find_max_sum_sublist(lst):
    if not lst:
        return []
    j = 0
    curr_max = -float('Inf')  # 12
    summ = 0  # 2
    while j < len(lst):
        summ += lst[j]
        curr_max = max(curr_max, summ)
        if summ < 0:
            summ = 0
        j += 1
    return curr_max
