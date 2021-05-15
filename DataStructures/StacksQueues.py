from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self, lst = None):
        self.top = None
        self.stack_size = 0
        if lst:
            for ele in lst:
                self.push(ele)

    def is_empty(self):
        return self.top == None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.stack_size += 1

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            self.stack_size -= 1
            return node.val
        return None

    def peek(self):
        if self.top:
            return self.top.val
        return None

    def size(self):
        return self.stack_size


class Queue:
    def __init__(self, lst=None):
        self.queue_front = None
        self.queue_rear = None
        self.queue_size = 0
        if lst:
            for val in lst:
                self.enqueue(val)

    def is_empty(self):
        return self.queue_size == 0

    def size(self):
        return self.queue_size

    def enqueue(self, val):
        node = Node(val)
        if self.is_empty():
            self.queue_rear = node
            self.queue_front = node
        else:
            self.queue_rear.next = node
            self.queue_rear = node
        self.queue_size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.queue_front
        self.queue_front = self.queue_front.next
        self.queue_size -= 1
        if self.is_empty():
            self.queue_rear = None
        return node.val

    def front(self):
        if self.is_empty():
            return None
        return self.queue_front.val

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_rear.val

'''
Time complexity: O(2n) = O(n)
Space complexity: O(2n) = O(n)
Return all binary numbers until the given number
'''
def find_bin(number):
    result = []
    queue = deque(['1']) # 1 10 11 100 101 110 111 1000 1001 1010 1011
    for _ in range(number): # 3
        curr = queue.popleft()
        result.append(curr)
        queue.append(curr+'0')
        queue.append(curr+'1')
    return result

'''
two stacks using a single list
'''
class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack = [None] * size
        self.top1 = -1
        self.top2 = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 == self.top2 - 1: # stack is full
            return None
        self.top1 += 1
        self.stack[self.top1] = value

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 == self.top2 - 1: # stack is full
            return None
        self.top2 -= 1
        self.stack[self.top2] = value

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 < 0:
            return None
        popped_element = self.stack[self.top1]
        self.top1 -= 1
        return popped_element

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 >= len(self.stack):
            return None
        popped_element = self.stack[self.top2]
        self.top2 += 1
        return popped_element


'''
Time complexity = O(n)
Space complexity = O(k)
reverse the first K elements of a queue
'''
def reverseK(queue, k):
    size = queue.size() # 10
    if not queue or k < 0 or k > size:
        return None
    stack = [] #
    for _ in range(k): # for k times
        stack.append(queue.dequeue())
    while stack:
        queue.enqueue(stack.pop()) # 6 7 8 9 10 5 4 3 2 1
    for _ in range(size-k):
        queue.enqueue(queue.dequeue())  # 5 4 3 2 1 6 7 8 9 10
    return queue

'''
Implemement a queue using stacks
Time complexity:
- enqueue: O(1)
- dequeue: on best case O(1), worst case O(n) 
'''
class NewQueue:
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []
        # Write your code here

    # Inserts Element in the Queue
    # Time complexity and space complexity: O(1)
    def enqueue(self, value):
        # enqueue at the top
        self.main_stack.append(value)

    # Removes Element From Queue
    # Time complexity: O(n)
    # Space complexity: O(n)
    def dequeue(self):
        # dequeue from the bottom
        if self.aux_stack:
            return self.aux_stack.pop()
        while self.main_stack:
            self.aux_stack.append(self.main_stack.pop())
        if self.aux_stack:
            return self.aux_stack.pop()
        return None

'''
Time complexity: O(n^2)
Space complexity: O(n)
Sort a stack using stacks
'''
def sort_stack(stack):
    if stack.is_empty():
        return stack

    temp_stack = []
    size = stack.size()
    need_to_order = size
    while need_to_order:
        curr_max = stack.pop()
        for _ in range(need_to_order - 1):
            curr = stack.pop()
            if curr > curr_max:
                temp_stack.append(curr_max)
                curr_max = curr
            else:
                temp_stack.append(curr)
        stack.push(curr_max)
        while temp_stack:
            stack.push(temp_stack.pop())

        need_to_order -= 1
    return stack


'''
stack every number
skip spaces
when an operation sign is finded, pop out 2 numbers, apply the operation and stack the result back

Time complexity: O(n)
Space complexity: O(n)
'''
def evaluate_post_fix(exp):
    stack = []
    for character in exp:
        if character == ' ':
            continue
        elif character.isdecimal():
            stack.append(int(character))
        else:
            if len(stack) < 2:
                return None
            first_operand = stack.pop()
            second_operand = stack.pop()
            if character == '*':
                stack.append(second_operand * first_operand)
            elif character == '/':
                stack.append(second_operand / first_operand)
            elif character == '+':
                stack.append(second_operand + first_operand)
            elif character == '-':
                stack.append(second_operand - first_operand)
    if not stack or len(stack) > 1:
        return None
    return stack.pop()


'''
Time complexity: O(n)
Space complexity: O(n)

traverse from the end
keep popping until not stack or stack.peek() <= lst[i]
update the lst[i] appropriately and append previous lst[i] to stack
lst: [6, 8, 8, 8, -1, -1]
stack: [8,6,4]

[6, 8, 8, 8, -1, -1]
8 6 4
'''
def next_greater_element(lst):
    stack = []
    for i in range(len(lst)-1, -1, -1):
        while stack and stack[-1] <= lst[i]:
            stack.pop()
        value = lst[i]
        if not stack:
            lst[i] = -1
        else:
            lst[i] = stack[-1]
        stack.append(value)
    return lst

'''
Time complexity: O(n)
Space complexity: O(n)
'''
def is_balanced(exp):
    stack = []
    parenthesis_map = {')': '(', '}': '{', ']': '['}
    open_brackets = set(parenthesis_map.values())
    for character in exp:
        if character in open_brackets:
            stack.append(character)
        elif parenthesis_map[character] != stack.pop():
            return False
    if not stack:
        return True
    return False

'''
Keeps a min_stack along with the original stack to store the minimum state, for each top of the original stack 
we have the minimum at the time of that top was added.

Time complexity: O(1) for push, pop and min
'''
class MinStack:
    # Constructor
    def __init__(self):
        self.stack = []
        self.minimums = []
        self.size = 0

    def pop(self):
        if not self.stack:
            return None
        self.size -= 1
        self.minimums.pop()
        return self.stack.pop


    # Pushes value into new stack
    def push(self, value):
        self.size += 1
        if not self.minimums or value < self.minimums[-1]:
            self.minimums.append(value)
        else:
            self.minimums.append(self.minimums[-1])
        self.stack.append(value)

    # Returns minimum value from new stack in constant time
    def min(self):
        if not self.minimums:
            return None
        return self.minimums[-1]


stack = Stack([1,2,3])
stack.push(0)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.size())
stack.push(5)
print(stack.peek())
print(stack.size())
print(stack.is_empty())

print()
queue = Queue([1,2,3])
queue.enqueue(0)
print(queue.dequeue())
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue.size())
queue.enqueue(5)
print(queue.front())
print(queue.rear())
print(queue.size())