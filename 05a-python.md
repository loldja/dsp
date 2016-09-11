# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

<i>How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?</i>

>> A list is a sequence of values, called <b>elements</b> or <b>items</b>. In C++ this data structure would be called an array. The order of items is consistent, i.e the values inside the list can be called by their index, and each index "maps to" one of the elements.

>> A tuple is also a sequence of values, indexed by integers. The key difference is that while lists a mutable, tuples are immutable. This means that it's not possible to modify an element of the tuple. For example, A[0] = '1' to reassign the value at index 0 would throw an error for a tuple, but not for a list.

>> Only immutable types such as tuples are "hashable" meaning you can use a hashtable algorithm to compute a key location. So only a tuple (or a string) can be used as a sequence of dictionary keys, NOT a list.

---

###Q2. Lists &amp; Sets

<i>How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?</i>

>> Lists and sets are both mutable, i.e. they can be changed. A set is an unordered collection of elements, and these elements must be immutable. It's possible to perform mathematical calculations on a set, such as union, intersection, etc. Unlike a  list, the elements within a set are unordered. Unlike a list, the elements of a set must be unique.

>> List syntax:
```
my_list = ['here', 'there', 'everywhere']
```

>> Set syntax:
```
my_set = {1, 2, 3}
```

>> Find an element within a set or a list using the <b>in</b> command; this will return True or False.



---

###Q3. Lambda Function

<i>Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.</i>

>> Lambda is the anonymous/ generic function. It can be defined "on the fly" but is limited to a quick local calculation. It should not be used if the function needs to be called globally, or multiple times.

>> Here's an example of how a lambda function can alter the sorting behavior: 

```
$ sorted('ah','Eh','aa','AA')
```
['AA', 'Eh', 'aa', 'ah']
```
$ sorted(('ah','Eh','aa','AA'),key=lambda word: word.lower())
```
['aa', 'AA', 'ah', 'Eh']


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a Pythonic alternative to loops with incrementing throwaway generators to move through each element in a list. `map` and `filter` also provide this functional ability using Python reserved words.  

>> Typical list comprehension:
```
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
# doubles every odd number in a list
```

>> Same functionality using `map` and `filter`:
```
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> Between 01-02-2013 and 07-28-2015 there are 937 days, 0:00:00 seconds

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> Between 12312013 and 05282015 there are 513 days, 0:00:00 seconds

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> Between 15-Jan-1994 and 14-Jul-2015 there are 7850 days, 0:00:00 seconds

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

