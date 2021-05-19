class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    '''Time complexity: O(n) where n is the size of the word'''
    def insert(self, word):
        if not word:
            return
        word = word.lower()

        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode(char)
            curr = curr.children[index]
        curr.is_end_word = True

    '''Time complexity: O(n) where n is the size of the word'''
    def search(self, word):
        if not word:
            return False
        word = word.lower()

        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            # print(curr.char, end=' ')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        # print(curr.char)
        if curr.is_end_word:
            return True
        return False

    '''Time complexity: O(n*k) where n is the size of the word and k is the size of the alphabet'''
    def remove(self, word):
        if not word:
            return
        word = word.lower()
        self.remove_unused_nodes(word, 0, self.root)

    def remove_unused_nodes(self, word, char_index, curr):
        if char_index == len(word):  # last character
            curr.is_end_word = False
            if not self.check_if_any_child(curr):
                return True

        index = ord(word[char_index]) - ord('a')
        if self.remove_unused_nodes(word, char_index + 1, curr.children[index]):
            curr.children[index] = None

        if not self.check_if_any_child(curr) and not curr.is_end_word:
            return True

    '''Same time and space complexity as the recursive way'''
    def remove_iterative(self, word):
        if not word:
            return False
        word = word.lower()
        ancestors = []  # stack
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            ancestors.append(curr)
            curr = curr.children[index]
        curr.is_end_word = False
        while ancestors:
            parent = ancestors.pop()
            if self.check_if_any_child(curr) or curr.is_end_word:
                return True
            curr_index = ord(curr.char) - ord('a')
            parent.children[curr_index] = None
            curr = parent
        return True

    def check_if_any_child(self, parent):
        if not parent:
            return
        for child in parent.children:
            if child != None:
                return True
        return False


'''
Time complexity: O(n) where n is the number of characters in the trie
Space complexity: O(n)
'''
def total_words(root):
    if not root:
        return 0
    summ = 0
    if root.is_end_word:
        summ += 1
    for child in root.children:
        if child:
            summ += total_words(child)
    return summ


'''
Retrieve every word in a trie
Time complexity: O(n) where n is the number of nodes in the trie
Space complexity: O(c+w) where w is the number of words and c is the number of characters in the longest word
'''
def find_words(root):
    if not root:
        return []
    result = []
    retrieve_all_words(root, '', result)
    return result


def retrieve_all_words(root, forming_word, result):
    new_word = forming_word + root.char
    if root.is_end_word:
        result.append(new_word)

    for child in root.children:
        if child:
            retrieve_all_words(child, new_word, result)


'''
Sort a list of strings using tries
Time complexity: O(n*c) where n is the number of words and c is the number of characters in the longest word
Space complexity: O(n+c)
'''
def sort_list(arr):
    trie = Trie()
    for word in arr:
        trie.insert(word)
    return find_words(trie.root)


'''
Find whether a given word can be formed by combining two words from a dictionary
Time complexity: O(m + n^2) where m is the size of the dictionary and n is the length of the word
Space complexity:O(m+n)
'''
def is_formation_possible(dictionary, word):
    trie = Trie()
    for w in dictionary:
        trie.insert(w)
    curr = trie.root
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if not curr.children[index]:
            return False
        elif curr.children[index].is_end_word:
            if trie.search(word[i+1:]):
                return True
        curr = curr.children[index]
    return True

'''
dictionary: ['hello', 'world', 'he']
word: 'helloworld'
This solution could find the possible formation using the n words in the dictionary, not only pairs
Time complexity: O(2^n)
Space complexity: O(2^n)
'''
def is_formation_possible_rec(dictionary, word):
    trie = Trie()
    for w in dictionary:
        trie.insert(w)
    return is_formation_possible_recursive(word, 0, trie.root, trie.root)


def is_formation_possible_recursive(word, letter_index, curr, root):
    if not curr:
        return False
    if letter_index == len(word):
        if curr.is_end_word:
            return True
        return False
    index = ord(word[letter_index]) - ord('a')
    if curr.is_end_word:
        return is_formation_possible_recursive(word, letter_index + 1, curr.children[index], root) \
               or is_formation_possible_recursive(word, letter_index + 1, root.children[index], root)

    return is_formation_possible_recursive(word, letter_index + 1, curr.children[index], root)


trie = Trie()
trie.insert('therefore')
# trie.insert('their')
trie.insert('the')
print(trie.search('therefore'))
# print(trie.search('their'))
print(trie.search('the'))
# trie.remove_iterative('therefore')
trie.remove('therefore')
print(trie.search('therefore'))
# print(trie.search('their'))
print(trie.search('the'))
new_trie = Trie()
new_trie.insert('Hello')
new_trie.insert('World')
new_trie.insert('HE')
print(is_formation_possible(['hello', 'world', 'he'], 'helloworld'))
print(is_formation_possible_rec(['hello', 'world', 'he'], 'helloworld'))
print(is_formation_possible_rec(['the', 'hello', 'there', 'answer', 'any', 'educative', 'world', 'their', 'abc'], 'helloworld'))
print(is_formation_possible_rec(['the', 'hello', 'there', 'answer', 'any', 'educative', 'world', 'their', 'abc'], 'educativeinc'))
print(is_formation_possible_rec(['the', 'hello', 'there','i','n','c', 'answer', 'any', 'educative', 'world', 'their', 'abc'], 'educativeinc'))
