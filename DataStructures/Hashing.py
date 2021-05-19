class HashEntry:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size=10, threshold=0.6):
        self.size = size
        self.curr_size = 0
        self.threshold = threshold
        self.buckets = [None] * self.size

    # Hash function: arithmetic modular
    def get_index(self, key):
        hash_code = hash(key)
        return hash_code % self.size

    def resize(self):
        new_size = self.size * 2
        new_buckets = [None] * new_size

        # reindexing every element into the new buckets array
        for head in self.buckets:
            while head:
                new_index = hash(head.key) % new_size
                new_entry = HashEntry(head.key, head.val)
                new_entry.next = new_buckets[new_index]
                new_buckets[new_index] = new_entry
                head = head.next

        self.size = new_size
        self.buckets = new_buckets

    def insert(self, key, value):
        index = self.get_index(key)
        if not self.buckets[index]:
            self.buckets[index] = HashEntry(key, value)
            self.curr_size += 1
            return
        prev = None
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next

        self.curr_size += 1
        prev.next = HashEntry(key, value)

        load_factor = self.curr_size/self.size
        if load_factor >= self.threshold:
            self.resize()

    def remove(self, key):
        index = self.get_index(key)
        if not self.buckets[index]:
            return
        if self.buckets[index].key == key:
            self.buckets[index] = self.buckets[index].next
            self.curr_size -= 1
            return
        prev = None
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.curr_size -= 1
                return
            prev = curr
            curr = curr.next

    def search(self, key):
        index = self.get_index(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

'''
Find if list2 is a subset of list1
Time complexity: O(m + n) where m is the size of list1 and n is the size of list2
Space complexity: O(n) that I am assuming will always be less than m
'''
def is_subset(list1, list2):
    lst2_set = set(list2)
    counter = 0
    for ele in list1:
        if ele in lst2_set:
            counter += 1
    return counter == len(lst2_set)


'''
check if the lists given are disjoint
Time complexity: O(m + n) where m is the size of list1 and n is the size of list2
Space complexity: O(m)
'''
def is_disjoint(list1, list2):
    lst1_set = set(list1)
    for ele in list2:
        if ele in lst1_set:
            return False
    return True


'''
Find all the symmetric pairs in a given list
Time complexity: O(n)
Space complexity: O(n)
'''
def find_symmetric(my_list):
    result = []
    pottential_symmetrics = set()
    for pair in my_list:
        symmetric_pair = (pair[1],pair[0])
        if symmetric_pair in pottential_symmetrics:
            result.append(list(pair))
            result.append(list(symmetric_pair))
        pottential_symmetrics.add(tuple(pair))
    return result


'''
take in a list of source-destination pairs and return the correct sequence of the 
whole journey from the first city to the last
Time complexity: O(n)
Space complexity: O(n)
'''
def trace_path(my_dict):  # A Map object
    # find source
    source = None
    for ele in my_dict.keys():
        if ele not in my_dict.values():
            source = ele
            break

    # trace the path
    result = []
    key = source
    while key in my_dict:
        result.append([key, my_dict[key]])
        key = my_dict[key]

    return result


'''
Find two pairs, [a, b] and [c, d], in a list such that : a+b = c+d and a+b=c+d
Time complexity: O(n^2)
Space complexity: O(n^2)
'''
def find_pair(my_list):
    pairs = {}
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            summ = my_list[i] + my_list[j]
            if summ in pairs:
                return [pairs[summ], [my_list[i], my_list[j]]]
            pairs[summ] = [my_list[i], my_list[j]]
    return None



'''
Find if there exists a sublist in which the sum of all elements is zero
Time complexity: O(n)
Space complexity: O(n)
'''
def find_sub_zero(my_list):
    # 2 2 4 5 -9 1
    previous_summ = set()
    summ = 0
    for num in my_list:
        summ += num
        if num == 0 or summ == 0 or summ in previous_summ:
            return True
        previous_summ.add(summ)
    return False


'''
Find whether a given word can be formed by combining two words from a dictionary
Time complexity: O(m + n^2) where m is the size of the dictionary and n is the length of the word, but in the worst case it would be O(m + m*n^2)
Space complexity:O(m+n)
'''
def is_formation_possible(lst, word):
    words_set = set(lst)
    for split_point in range(1, len(word)):
        if word[split_point:] in words_set and word[:split_point] in words_set:
            return True
    return False


'''
Find two numbers that add up to the target
Time complexity: O(n)
Space complexity: O(n)
'''
def findSum(lst, k):
    pairs = {}
    for num in lst:
        if num in pairs:
            return [num, pairs[num]]
        pairs[k-num] = num
    return None


'''
Time complexity: O(n)
Space complexity: O(n)
'''
def findFirstUnique(lst):
    occurrences = {num:0 for num in lst}
    for num in lst:
        occurrences[num] += 1
    # check for unique
    for num in lst:
        if occurrences[num] == 1:
            return num
    return None


'''
Time complexity: O(n)
Space complexity: O(n)
Note: Floyd's algorithm to detect loop is a better approach
'''
def detect_loop(lst):
    visited = set()
    curr = lst.get_head()
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next_element
    return False


'''
Time complexity: O(n)
Space complexity: O(n)
'''
def remove_duplicates(lst):
    visited = set()
    prev = None
    curr = lst.get_head()
    while curr:
        if curr.data in visited:
            prev.next_element = curr.next_element
        else:
            prev = curr
        visited.add(curr.data)
        curr = curr.next_element


'''
Time complexity: O(n+m)
Space complexity: O(n)

21 7 15 20 14
          ^
14 7 21
        ^
        ^
Notes: Put in place on list1 every element that is not repeated from list2
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
Notes: Remove in place on list2 every element that is not an intersection with list1
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
Find the longest substring with k unique characters in a given string

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message. 

Time complexity: O(n)
Space complexity: O(n)
'''
def longest_sub_k_unique(str, k):
    if not str or k <= 0: # aabbcc k=1
        return ''
    max_len = 0
    longest_sub = ''
    start = 0
    end = 0
    uniques = set()
    while end < len(str):
        uniques.add(str[end])
        if len(uniques) == k:
            max_len = max(max_len, end-start+1)
            longest_sub = str[start:end+1]
        while len(uniques) > k:
            # could be done counting the occurrences into a hash_map, maybe this part would be more readable
            uniques.remove(str[start])
            start += 1
            uniques.add(str[start])
        end += 1
    return longest_sub


hashtable = HashTable()
hashtable.insert('hey', 1)
hashtable.insert('hi', 2)
hashtable.insert('ohio', 3)
print(hashtable.search('hey'))
print(hashtable.search('hi'))
print(hashtable.search('ohio'))
hashtable.remove('hey')
print(hashtable.search('hey'))
print(hashtable.search('hi'))
print(hashtable.search('ohio'))
hashtable.remove('ohio')
print(hashtable.search('hey'))
print(hashtable.search('hi'))
print(hashtable.search('ohio'))
hashtable.remove('hi')
print(hashtable.search('hey'))
print(hashtable.search('hi'))
print(hashtable.search('ohio'))
# testing resizing
print(len(hashtable.buckets), hashtable.curr_size)
for c in 'acbdefghijklmnopqrstuvwx':
    hashtable.insert(c,'whatever')
    # print(len(hashtable.buckets), hashtable.curr_size)
print(len(hashtable.buckets), hashtable.curr_size, len('acbdefghijklmnopqrstuvwx'))
for c in 'acbdefghijklmnopqrstuv':
    hashtable.remove(c)
    # print(len(hashtable.buckets), hashtable.curr_size)
print(len(hashtable.buckets), hashtable.curr_size)
print(hashtable.buckets)
print(is_formation_possible(['hey'], 'hey'))
print(is_formation_possible(['he', 'y'], 'hey'))
print(longest_sub_k_unique("aabbcc", 1))
print(longest_sub_k_unique("aabbcc", 2))
print(longest_sub_k_unique("aabbcc", 3))
print(longest_sub_k_unique("aaabbb", 3))