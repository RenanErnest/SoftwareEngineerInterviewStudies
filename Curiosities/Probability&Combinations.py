'''
https://www.mathsisfun.com/combinatorics/combinations-permutations.html
'''
import random

# Return all permutations
# Time complexity: O(n^n), exponential
# Space complexity: O(n^n), exponential
def permutations(s, comb, res):
    if len(comb) == len(s):
        res.append(comb)
        return

    for i in range(len(s)):
        permutations(s, comb + s[i], res)

    return res


# Return all permutations without repetition
# Time complexity: O(n!), factorial
# Space complexity: O(n!), factorial
# example: produce all anagrams
def permutations_no_repetition(s, comb, res):
    if len(s) == 0:
        res.append(comb)
        return

    for i in range(len(s)):
        permutations_no_repetition(s[:i] + s[i+1:], comb + s[i], res)

    return res

# used as inspiration for permutations without repetition
'''
https://stackoverflow.com/questions/11989502/producing-all-the-anagrams-from-a-string-python/40519177
'''
def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

# Return all combinations
# Time complexity: O(2^n), exponential, tighter bound = O(n^min{k,n-k})
# Space complexity: O(2^n), exponential, tighter bound = O(n^min{k,n-k})
def combinations(s, index, comb, res):
    if len(comb) == len(s):
        res.append(comb)
        return

    for i in range(index, len(s)):
        combinations(s, i, comb + s[i], res)

    return res

# Return all combinations without repetition
def combinations_no_repetition(n, r, index, comb, res):
    if len(comb) == r:
        res.append(comb)
        return

    for i in range(index+1, len(n)):
        combinations_no_repetition(n, r, i, comb + n[i], res)

    return res


# Pascale Ricketts' 3 Rolls to Ten
def three_rolls_to_ten(experiments=1000000):
    average = 0
    for _ in range(experiments):
        rolls = [random.randint(1, 6) for i in range(3)]
        if sum(rolls) >= 10:
            average += 1
    average /= experiments
    return average


# print(three_rolls_to_ten())
res = permutations('123', '', [])
print(res, len(res))

res = permutations_no_repetition('123', '', [])
print(res, len(res))

res = combinations('123', 0, '', [])
print(res, len(res))

res = combinations_no_repetition('12345', 3, -1, '', [])
print(res, len(res))
