import heapq

class MaxHeap:
    def __init__(self, lst=[]):
        self.heap = lst
        for i in range(len(self.heap)-1,-1,-1):
            self.__heapify(i)

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap)-1)

    def remove(self):
        if not self.heap:
            return
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__heapify(0)
        return value

    def __percolate_up(self, index):
        if index <= 0:
            return
        parent_index = (index-1) // 2
        if self.heap[index] > self.heap[parent_index]:
            aux = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = aux
            self.__percolate_up(parent_index)

    def __heapify(self, index):
        if index >= len(self.heap):
            return
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index
        if largest_index != index: # check the need to swap and continue to heapify
            aux = self.heap[index]
            self.heap[index] = self.heap[largest_index]
            self.heap[largest_index] = aux
            self.__heapify(largest_index)


class MinHeap:
    def __init__(self, lst=[]):
        self.heap = lst
        for i in range(len(self.heap)-1, -1, -1):
            self.__heapify(i)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap)-1)

    def remove(self):
        if not self.heap:
            return None
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__heapify(0)
        return value

    def __percolate_up(self, index):
        if index <= 0:
            return
        parent_index = (index-1)//2
        if self.heap[index] < self.heap[parent_index]:
            aux = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = aux
            self.__percolate_up(parent_index)

    def __heapify(self, index):
        if index >= len(self.heap):
            return
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest_index = right_child_index
        if smallest_index != index:
            aux = self.heap[index]
            self.heap[index] = self.heap[smallest_index]
            self.heap[smallest_index] = aux
            self.__heapify(smallest_index)


'''
Convert a max heap into a min heap and return it in a form of a string
Time complexity: O(n), build a heap time complexity
Space complexity: O(1)
'''
def convertMax(maxHeap):
    for i in range(len(maxHeap)-1, -1, -1):
        min_heapify(maxHeap, i)
    return maxHeap

def min_heapify(heap, index):
    if index >= len(heap):
        return
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    smallest_index = index
    if left_child_index < len(heap) and heap[left_child_index] < heap[smallest_index]:
        smallest_index = left_child_index
    if right_child_index < len(heap) and heap[right_child_index] < heap[smallest_index]:
        smallest_index = right_child_index
    if smallest_index != index:
        aux = heap[index]
        heap[index] = heap[smallest_index]
        heap[smallest_index] = aux
        min_heapify(heap, smallest_index)


'''
Time complexity: O(n + k*log n), n to build the heap and k number of pops from the heap
Space complexity: O(k)
'''
def findKSmallest(lst, k):
    heapq.heapify(lst)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(lst))
    return result

'''
Time complexity: O(n + k*log n), n to build the heap and k number of pops from the heap
Space complexity: O(k)
'''
def findKLargest(lst, k):
    for i in range(len(lst)):
        lst[i] *= -1
    heapq.heapify(lst)
    result = [-1 * heapq.heappop(lst) for _ in range(k)]
    return result


heap = MaxHeap([5,1,2,54,6,8,1,3,54,6,9,0,4])
while heap.heap:
    print(heap.remove(), end=' ')
print()
heap = MaxHeap([1,2,3,4,5])
heap.insert(10)
heap.insert(3)
heap.insert(-1)
print(heap.get_max())
while heap.heap:
    print(heap.remove(), end=' ')
print()

heap = MinHeap([5,1,2,54,6,8,1,3,54,6,9,0,4])
while heap.heap:
    print(heap.remove(), end=' ')
print()
heap = MinHeap([1,2,3,4,5])
heap.insert(10)
heap.insert(3)
heap.insert(-1)
print(heap.get_min())
while heap.heap:
    print(heap.remove(), end=' ')
print()