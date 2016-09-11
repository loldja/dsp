# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

print "DONUTS FUNCTION TESTS"

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count >= 10:
        print 'Number of donuts: many'
    else:
        print 'Number of donuts: ' + str(count)

##test cases
donuts(5)
donuts(12)

print "BOTH_ENDS FUNCTION TESTS"

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if(len(s)<2):
        return ''
    else:
        return (s[0] + s[1] + s[-2] + s[-1])

#test cases
print both_ends('spring')
print both_ends('lauren oldja')
print both_ends('t')
print both_ends('to')

print "FIX_START FUNCTION TESTS"

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_letter = s[0]
    new_string = ''
    for letter in s: 
        if letter == first_letter:
            new_string += '*'
        else:
            new_string += letter
    return first_letter + new_string[1:]

print fix_start('babble')
print fix_start('aardvark')
print fix_start('google')

print "MIX_UP FUNCTION TESTS"

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    mix_temp = a[0:2]
    a = b[0:2] + a[2:]
    b = mix_temp + b[2:]
    return a, b

print mix_up('dog', 'dinner')
print mix_up('chocolate','stop sign')
print mix_up('rainbow','butterfly')

print "VERBING FUNCTION TESTS"

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[-3:]=="ing":
            s += "ly"
        else:
            s += "ing"

    return s

print verbing('hail')
print verbing('swimming')
print verbing('go')


print "NOT_BAD FUNCTION TESTS"

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    start_index = s.lower().find("not")
    end_index = s.lower().find("bad")+3
    if end_index < start_index:
        return s
    elif start_index == 0:
        return s[:start_index] + 'Good' + s[end_index:] 
    else:
        return s[:start_index] + 'good' + s[end_index:]
    
print not_bad('This movie is not so bad')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")
print not_bad('This dinner is not that bad')
print not_bad('Not bad deal')


print "FRONT_BACK FUNCTION TESTS"

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    if len(a) % 2 == 1:
        a_length = len(a)/2+1
    else:
        a_length = len(a)/2
    if len(b) % 2 == 1:
        b_length = len(b)/2+1
    else:
        b_length = len(b)/2
    return a[:a_length] + b[:b_length] + a[a_length:] + b[b_length:]

print front_back('abcde','xyz')
print front_back('abcd','xy')
print front_back('Kitten','Donut')
print front_back('potato','pumpkin')