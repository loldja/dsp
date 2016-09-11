# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count += 1
    return count
    
print "TEST MATCH_ENDS FUNCTION"
print match_ends(['aba','xyz','aa','x','bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    x_words = [] #empty list initialize
    no_x_words = []
    words.sort()
    for word in words:
        if word[0]=='x':
            x_words.append(word)
        else:
            no_x_words.append(word)

    return x_words + no_x_words

print "TEST FRONT_X FUNCTION"
print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark','zzz'])

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    def getKey(item):
        return item[1]
    tuples.sort(key=getKey)
    return tuples

print "TEST SORT_LAST FUNCTION"
print sort_last([(1, 3), (3, 2), (2, 1)])
print sort_last([(2, 3), (1, 2), (3, 1)])
print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    to_be_removed = []
    for i in range(len(nums)):
        if i == 0:
            continue
        if nums[i]==nums[i-1]:
            to_be_removed.append(i)

    to_be_removed.sort(reverse=True)
    for item in to_be_removed:
        del nums[item]

    return nums


print "TEST REMOVE_ADJACENT FUNCTION"
print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])
print remove_adjacent([3, 2, 3, 3, 3])
print remove_adjacent([])


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    merged_list = []
    i = 0
    j = 0
    count = 0

    while count < (len(list1) + len(list2)):
        if len(list1) == i:
            merged_list.append(list2[j])
            j += 1
        elif len(list2) == j:
            merged_list.append(list1[i])
            i += 1

        elif list1[i]<list2[j]:
            merged_list.append(list1[i])
            i+=1

        else:
            merged_list.append(list2[j])
            j+=1

        count +=1


    return merged_list


print "LINEAR_MERGE FUNCTION TESTS"
print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
print linear_merge(['xx', 'xx'], ['bb', 'bb', 'bb'])

