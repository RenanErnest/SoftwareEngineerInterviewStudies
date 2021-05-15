class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head == None

    def insert(self, val):
        curr = Node(val)
        curr.next = self.head
        self.head = curr

    def insert_tail(self, val):
        if not self.head:
            self.insert(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def insert_kth(self, k, val):
        if k == 0:
            self.insert(val)
            return
        i = 1
        curr = self.head
        while curr.next:
            if i == k:
                node = Node(val)
                node.next = curr.next
                curr.next = node
                return True
            i += 1
            curr = curr.next

        if i == k:
            node = Node(val)
            node.next = curr.next
            curr.next = node
            return True
        return False

    def size(self):
        n = 0
        curr = self.head
        while curr:
            n += 1
            curr = curr.next
        return n

    def remove(self, val):
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return True
            curr = curr.next

        return False

    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end='->')
            curr = curr.next
        print('None')

'''
Time complexity: O(n)
Space complexity: O(1)
'''
def reverse_linked_list(lst):
    if not lst.get_head():
        return None

    prev = None
    curr = lst.get_head()
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    lst.head = prev
    return lst


'''
Time complexity: O(n)
Space complexity: O(1)
Floyd's cycle-finding algorithm
'''
def detect_loop(lst):
    one_step = lst.get_head()
    two_step = lst.get_head()
    while one_step and two_step and two_step.next:
        one_step = one_step.next
        two_step = two_step.next.next
        if one_step == two_step:
            return True

    return False

'''
Time complexity: O(n)
Space complexity: O(n)
'''
def detect_loop_hash(lst):
    visited = set()
    curr = lst.head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False


'''
Time complexity: O(n)
Space complexity: O(1)

7->14->10->21->22
        ^
                  ^
'''
def find_mid(lst):
    if not lst or not lst.get_head():
        return None
    onestep = lst.get_head()
    twostep = onestep.next
    while onestep and twostep and twostep.next:
        onestep = onestep.next
        twostep = twostep.next.next
    return onestep.val


'''
Time complexity: O(n)
Space complexity: O(n)
'''
def remove_duplicates(lst):
    if not lst or not lst.get_head():
        return None

    visited = set()
    prev = None
    curr = lst.get_head()
    while curr:
        if curr.val in visited:
            prev.next = curr.next
        else:
            visited.add(curr.val)
            prev = curr
        curr = curr.next


'''
Time complexity: O(n+m)
Space complexity: O(n)

21 7 15 20 14
          ^
14 7 21
        ^
        ^
'''
def union(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    visited = set()  # 15 20 14
    curr = list1.get_head()
    while curr:
        visited.add(curr.data)
        curr = curr.next_element

    curr = list2.get_head()
    next = None
    while curr:
        next = curr.next_element
        if curr.data not in visited:
            curr.next_element = list1.head_node
            list1.head_node = curr
        curr = next

    return list1

'''
Time complexity: O(n+m)
Space complexity: O(n)
'''
def intersection(list1, list2):
    if not list1 or not list2:
        return None

    visited = set()
    curr = list1.get_head()
    while curr:
        visited.add(curr.data)
        curr = curr.next_element

    while list2.head_node and list2.head_node.data not in visited:
        list2.head_node = list2.head_node.next_element

    prev = None
    curr = list2.get_head()
    while curr:
        if curr.data not in visited:  # remove from the list
            prev.next_element = curr.next_element
        else:
            prev = curr
        curr = curr.next_element

    return list2


'''
Time complexity: O(n)
Space complexity: O(1)

Return the nth last element

steps: 0
5 22 8 7 14 21
     ^
'''
def find_nth(lst, n):
    if not lst:
        return -1

    size = lst.queue_size()
    steps = size - n
    if steps < 0:
        return -1
    curr = lst.get_head()
    while curr and steps > 0:
        steps -= 1
        curr = curr.next_element
    return curr.data

'''
Time complexity: O(n)
Space complexity: O(1)
'''
def find_nth_twopointers(lst, n):
    if not lst:
        return -1

    endpointer = lst.get_head()
    rightpointer = lst.get_head()

    while n > 0:
        if not endpointer:
            return -1
        n -= 1
        endpointer = endpointer.next

    while endpointer:
        endpointer = endpointer.next
        rightpointer = rightpointer.next

    return rightpointer.val

lst = LinkedList()
lst.insert(2)
lst.insert(6)
lst.insert(1)
lst.insert(0)
print(lst.search(2), lst.search(7))
print(lst.remove(2))
print(lst.search(2))
lst.insert_tail(5)
lst.print()
lst.insert_kth(4, 9)
print(lst.size())
lst.print()
reverse_linked_list(lst)
lst.print()