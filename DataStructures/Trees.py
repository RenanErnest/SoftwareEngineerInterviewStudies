"""
A tree is a connected graph with no cycles

Degree of a node: number of children
Depth of a node: the length from the root to the node. The depth of the root itself is 0
Height of a node: the length from the node to its deepest descendant. The height of leaf nodes is 0

Balanced tree: the height of each node follows abs(height(LeftSubTree) - height(RightSubTree)) < 2
Perfect binary tree: full of nodes
Total number of nodes: 2^(h+1) -1
Total number of Leaf nodes: 2^h or (n+1)/2

Balanced trees are good to perform operations and skewed trees should be avoided

Binary Search Trees (BST): NodeValues(leftsubtree) <= CurrentNodeValue < NodeValues(rightsubtree)
Red-black trees height: h <= 2log2(n+1)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
Time complexity: O(n) in the worst case of a skewed tree, O(log n) in case of the tree is balanced, where n is the number of nodes
Space complexity: O(n)
'''
def bst_insert_recursive(root, val):
    if not root:
        return

    if val >= root.val:
        if root.right:
            bst_insert_recursive(root.right, val)
        else:
            root.right = Node(val)
            return
    else:
        if root.left:
            bst_insert_recursive(root.left, val)
        else:
            root.left = Node(val)
            return


'''
Time complexity: O(n) in the worst case (skewed tree), O(log n) in case of the tree is balanced, where n is the number of nodes
Space complexity: O(1)
'''
def bst_insert_iterative(root, val):
    while root:
        if val >= root.val:
            if root.right:
                root = root.right
            else:
                root.right = Node(val)
                return
        else:
            if root.left:
                root = root.left
            else:
                root.left = Node(val)
                return


'''
Time complexity: O(n) in the worst case, O(log n) in case of the tree is balanced, where n is the number of nodes
Space complexity: O(1)
'''
def bst_search(root, val):
    while root:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root

    return None


def bst_search_recursive(root, val):
    if not root:
        return None

    if val < root.val:
        return bst_search_recursive(root.left, val)
    elif val > root.val:
        return bst_search_recursive(root.right, val)
    else:
        return root

'''
Time complexity: O(n) in the worst case, O(log n) in case of the tree is balanced, where n is the number of nodes
Space complexity: idem
'''
def bst_delete_recursive(root, val):
    if not root:
        return None

    if val < root.val:
        root.left = bst_delete_recursive(root.left, val)
    elif val > root.val:
        root.right = bst_delete_recursive(root.right, val)
    else:  # val was found in the tree
        if not root.left and not root.right:  # leaf node
            return None
        elif not root.right:  # root has just the left child
            return root.left
        elif not root.left:  # root has just the right child
            return root.right
        else:  # root has two children
            to_be_deleted = root.right
            while to_be_deleted.left:
                to_be_deleted = to_be_deleted.left
            root.val = to_be_deleted.val
            root.right = bst_delete_recursive(root.right, to_be_deleted.val)
    return root

'''
Time complexity: O(n) in the worst case, O(log n) in case of the tree is balanced, where n is the number of nodes
Space complexity: O(1)
'''
def bst_delete_iterative(root, val):
    if not root:
        return None
    parent = None
    curr_node = root
    while curr_node:
        if val < curr_node.val:
            parent = curr_node
            curr_node = curr_node.left
        elif val > curr_node.val:
            parent = curr_node
            curr_node = curr_node.right
        else: # value found
            if not curr_node.left and not curr_node.right:
                if not parent: # delete the root
                    return None
                if parent.left == curr_node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            if not curr_node.left:
                if not parent:
                    return curr_node.right
                if parent.left == curr_node:
                    parent.left = curr_node.right
                else:
                    parent.right = curr_node.right
                return root
            if not curr_node.right:
                if not parent:
                    return curr_node.left
                if parent.left == curr_node:
                    parent.left = curr_node.left
                else:
                    parent.right = curr_node.left
                return root
            else: # has two children
                to_be_deleted = curr_node.right
                parent = curr_node
                while to_be_deleted.left:
                    parent = to_be_deleted
                    to_be_deleted = to_be_deleted.left
                curr_node.val = to_be_deleted.val
                if parent.left == to_be_deleted:
                    parent.left = None
                else:
                    parent.right = None
                return root
    return root


def preorder_traversal(root, result):
    if not root:
        return
    result.append(root.val)
    preorder_traversal(root.left, result)
    preorder_traversal(root.right, result)
    return result


def inorder_traversal(root, result):
    if not root:
        return
    inorder_traversal(root.left, result)
    result.append(root.val)
    inorder_traversal(root.right, result)
    return result


def postorder_traversal(root, result):
    if not root:
        return
    postorder_traversal(root.left, result)
    postorder_traversal(root.right, result)
    result.append(root.val)
    return result

'''
Find minimum value in a BST
Time complexity: O(n) in the worst case, O(log n) in the case of a balanced tree
Space complexity: O(1)
'''
def findMin(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val


'''
Time complexity: O(n)
Space complexity: O(n)
'''
def findKthMax(root, k):
    if k < 1:
        return None

    global counter
    counter = 0
    return findKthMaxRecursive(root, k)


def findKthMaxRecursive(root, k):
    global counter
    if not root:
        return None

    maxi = findKthMaxRecursive(root.rightChild, k)
    if maxi:
        return maxi
    counter += 1
    if counter == k:
        return root.val
    maxi = findKthMaxRecursive(root.leftChild, k)
    if maxi:
        return maxi


'''
Time complexity: O(n)
Space complexity: O(n)

In case of a bst the recursive part could be altered by going towards just the correct path, this would made the time 
complexity O(log n) in best case 
'''
def findAncestors(root, k):
    ancestors = []
    findAncestorsRecursive(root, k, ancestors)
    return ancestors


def findAncestorsRecursive(root, k, ancestors):
    if not root:
        return False
    if root.val == k:
        return True
    if findAncestorsRecursive(root.leftChild, k, ancestors) or findAncestorsRecursive(root.rightChild, k, ancestors):
        ancestors.append(root.val)
        return True
    return False


'''
Time complexity: O(n)
Space complexity: O(n)
'''
def findHeight(root):
    if not root:
      return -1
    return 1 + max(findHeight(root.leftChild), findHeight(root.rightChild))


'''
Time complexity: O(n) in the worst case and O(2^(k+1) - 1) < n in the best case (balanced tree)
Space complexity: O(n) in the worst case and O(log n) in the best case (balanced tree)

Could be done also by using a bfs traversal by level technique where the space complexity would be O(2^k) < n
'''
def findKNodes(root, k):
    nodesAtKthLevel = []
    findNodesAtKthLevel(root, k, nodesAtKthLevel)
    return nodesAtKthLevel


def findNodesAtKthLevel(root, k, result):
    if not root:
        return False
    if k == 0:
        result.append(root.val)
        return True
    findNodesAtKthLevel(root.leftChild, k - 1, result)
    findNodesAtKthLevel(root.rightChild, k - 1, result)


class FourAryTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 4

    def print(self):
        print(self.val, end='')
        for child in self.children:
            if child:
                child.print()


'''
Serialize and deserialize n-ary tree
Time complexity: O(n) where n is the number of nodes in the tree
Space complexity: O(n)
'''
def serialize(root):
    return serialize_recursive(root, '')

def serialize_recursive(root, s):
    if not root:
        return ''
    s += str(root.val)
    for i in range(len(root.children)):
        if root.children[i]:
            s = serialize_recursive(root.children[i], s)
        else:
            s += '|'

    return s


def deserialize(s):
    if not s:
        return None
    global index
    index = 0
    return deserialize_recursive(s)


def deserialize_recursive(s):
    global index
    root = FourAryTreeNode(s[index])
    index += 1
    for i in range(len(root.children)):
        if index < len(s) and s[index] != '|':
            root.children[i] = deserialize_recursive(s)
        else:
            index += 1
    return root


'''
Find the inorder successor of determined key in a bst
Time complexity: O(n)
Space complexity: O(n)
'''
def find_inorder_successor(root, key):
    global found, successor
    found = False
    successor = None
    retrieve_inorder_successor(root, key)
    return successor


def retrieve_inorder_successor(root, key):
    if not root:
        return None

    global found, successor

    retrieve_inorder_successor(root.left)

    if root.val == key:
        found = True

    retrieve_inorder_successor(root.right)

    if found:
        successor = root.val
        found = False

'''
- find the key
- if the key has a right child: find the left-most node of the right child and return it
- if the key has no right child: in this case we should return its first grandparent that is greater than it

Note: I realized I can search the key storing the potential successor in the case the key_node doesn't have a right child

Time complexity: O(d) where d is level of the tree where the inorder successor of the key is found, in the worst case O(n)
Space complexity: O(1)
'''
def find_inorder_successor_iterative(root, key):
    # search the key alongside with keeping the potential successor
    potential_successor = None
    key_node = root
    while key_node:
        if key < key_node.val:
            potential_successor = key_node.val
            key_node = key_node.left
        elif key > key_node.val:
            key_node = key_node.right
        else:
            break
    if not key_node:
        return None

    if key_node.right:
        return most_left_child(key_node.right)

    return potential_successor


def most_left_child(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root


def calculate_cost_of_building_a_full_binary_tree(arr):
    cost = 0
    while len(arr) > 1:
        minimum = min(arr)
        min_index = arr.index(minimum)
        if min_index > 0 and min_index < len(arr)-1:
            cost += arr[min_index] * min(arr[min_index-1], arr[min_index+1])
        elif min_index < len(arr)-1:
            cost += arr[min_index] * arr[min_index+1]
        else:
            cost += arr[min_index] * arr[min_index-1]
        arr.pop(min_index) # removing the minimum value to prevent it to participate in future calculus
    return cost


root = Node(5)
bst_insert_iterative(root, 3)
bst_insert_iterative(root, 7)
bst_insert_recursive(root, 10)
bst_insert_recursive(root, 6)
print(bst_search(root, 10))
print(bst_search_recursive(root, 7))
print(preorder_traversal(root, []))
print(inorder_traversal(root, []))
print(postorder_traversal(root, []))

root = bst_delete_recursive(root, 7)
root = bst_delete_recursive(root, 11)
root = bst_delete_recursive(root, 6)
root = bst_delete_recursive(root, 5)
root = bst_delete_recursive(root, 10)
root = bst_delete_recursive(root, 3)

# root = bst_delete_iterative(root, 7)
# root = bst_delete_iterative(root, 11)
# root = bst_delete_iterative(root, 6)
# root = bst_delete_iterative(root, 5)
# root = bst_delete_iterative(root, 10)
# root = bst_delete_iterative(root, 3)

print(bst_search(root, 7))
print(bst_search(root, 6))
print(bst_search(root, 10))
print(bst_search(root, 3))
print(bst_search(root, 5))

fourAryTree = 'ABE|FK|||C|DG|H|I|J||||||||||||Y||||||||||||||'
root = deserialize(fourAryTree)
print(root.print(), fourAryTree, serialize(root), serialize(root) == serialize(deserialize(serialize(root))))

print(calculate_cost_of_building_a_full_binary_tree([4,6,2]))
print(calculate_cost_of_building_a_full_binary_tree([2,1]))
print(calculate_cost_of_building_a_full_binary_tree([5,3,1]))
print(calculate_cost_of_building_a_full_binary_tree([1,5,3]))
