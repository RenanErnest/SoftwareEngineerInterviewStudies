'''
Time complexity: O(nlogn) where n is the number os elements in the list
Space complexity: O(n)
'''
def merge_sort(lst):
    if len(lst) < 2:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    l = 0 # index for left half
    r = 0 # index for right half
    k = 0 # index of for sorted entire lst
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            lst[k] = left[l]
            l += 1
        else:
            lst[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        lst[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        lst[k] = right[r]
        r += 1
        k += 1


'''
Time complexity: O(nlogn) on average, it depends upon the data and the strategy for selecting a pivot. In the worst case
it could be O(n^2)
Space complexity: O(logn)
'''
# Good use case to test: [6,8,4,1,7,5]
def quick_sort(lst):
    quick_sort_recursive(lst,0, len(lst)-1)


def quick_sort_recursive(lst, low, high):
    if low >= high:
        return
    pivot_index = partition(lst, low, high)
    quick_sort_recursive(lst, pivot_index+1, high)
    quick_sort_recursive(lst, low, pivot_index-1)


def partition(lst, low, high):
    pivot = lst[high] # taking the last element as the pivot
    smaller_index = low # responsible for storing every element smaller than the pivot
    for i in range(low,high):
        if lst[i] < pivot:
            aux = lst[smaller_index]
            lst[smaller_index] = lst[i]
            lst[i] = aux
            smaller_index += 1
    aux = lst[smaller_index]
    lst[smaller_index] = lst[high]
    lst[high] = aux
    return smaller_index # the index of the pivot


lst = [6,8,4,1,7,5]
quick_sort(lst)
print(lst)
lst = [6,8,4,1,7,5]
merge_sort(lst)
print(lst)
