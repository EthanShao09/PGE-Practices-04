import time

# practices 04

# Common input format
# -------------------
# (Read the tasks descriptions below before reading this paragraph.)
# All tasks in practices 04 set share common data input format:
# The first line contains the number of the task (1 - 5).
# The second line contains the number N of lists in the input.
# In tasks 1-4, 0 < N < 6.  In task 5, 0 < N < 12 and N is even.
# Next, there are N lines of input, each contains one input list.
# Each list consists only of integers. List entries are separated by single space,
# there are no other symbols on the input line .
# The input always contain exactly one data set of one task.
# In the evaluation system, the code is run repeatedly, each time with different input.

# Solution code structure
# -----------------------
# The code reads the input data, including the number of the task.
# Next, it runs a function or a block of code which accepts the input data
# and computes and prints the solution to it.
# It is recommended to wrap the solution of each task in a separate function,
# an example (not obligatory!) structure of the code
# is illustrated by the contents of this file.


# ================================================================================
# Task 01

#
'''
Importances of Local Minima

A **local minimum** in a list of integers L is an item which value is smaller than
the value of both of its immediate neighbours. 
The first and the last item in the list cannot be a local minimum, in this task.
A **global maximum** of the list is an item which value is maximum in the
whole list.
Note that there may be more local minima and more global maxima in one list.
Example: L = [10, 9, 8, 7, 10, 1, 4, 9, 7, 8]. 
Local minima are 7, 1, 7, at indexes 3, 5, 8, respectively, global maxima
are 10 and 10 at indexes 0, 4, respectively.  

The **distance** between two items in the list is equal to the absolute
value of the difference of their indexes in the array. For example,
the distance between two adjacent items is 1, the distance between 
the first and the last item in a list L is len(L)-1. 

An **importance** of an item in the list is its minimum distance to a global maximum.
Example: L = [10, 9, 8, 7, 10, 1, 4, 9, 7, 8], the importances of particular items
         are [ 0, 1  2, 1,  0, 1, 2, 3, 4, 5].

The task:
Compute the total value of importances of all Local minima in the list.
For each given list, print the total value of importances on a separate line.
If there is no Local minimum in the list, output 0.
The length of each input list is at most 10000.

Example
  Input
1
3
10 9 8 7 10 1 4 13 7 8
2 4 2 4 2 4 2 4
40 30 20 10 20 30 40 30 20 10 20 30 40
  Output
7
3
6
  

Sentinels hint:
If your solutions stores the locations of global minima  in a separate list,
you may add sentinels representing imaginary non-existing maxima beyond the
scope of the list, far to the left and far to the right of the list. 
Sliding window hint:
As you move through the local minima in the list
you may incorporate the sliding window idea
The window would slide through the list and it would contain two current
global maxima between which the current local minimum is located.   

'''

def task01( L ):
    # your solution here
    pass

'''
# ------------------------------------------------------------------------------
Task02

Qualities of Local Minima

The notion of a local minimum and its importance is defined in the previous task.
This task uses the same definitions.
When a local minimum in a list L appears at index k, its depth is equal to
the smaller of the two differences a[k-1] - a[k], a[k+1] - a[k].
Each local minimum M is associated with a tuple of three parametres:
    The depth of M,
    the importance of M,
    the value of M.
This tuple associated with M is called quality of M.

Comparison of the qualities of two local minima M1 and M2 is done be the following scheme
    The minimum with bigger depth has a bigger quality than the other one.
    When the depths M1 and M2 are equal, the minimum with
    the bigger importance has a bigger quality than the other one.
    When  depths  and importances of the minima are equal, the minimum with
    smaller value has a bigger quality than the other one.
    When  depths, importances, and values of the minima are equal,
    the qualities of the minima are considered to be equal.    

The task:
  For a given list L of integers, print the list of its local minima 
  sorted in non-ascending order of their quality.
  When the quality of two minima is the same, the minima should appear in the output list
  in the same order as they appear in L.
  Each minimum M is printed on a separate line as a 4-tuple consisting
  of: index of M in L, depth of M, importance of M, value of M.
  The entries on a line are separated by single spaces and the line contains no other symbols.
  Print one empty line after the output list.


Example
  Input
2
3
10 9 8 7 10 1 4 13 7 8
2 4 2 4 2 4 2 4
40 30 20 10 20 30 40 30 20 10 20 30 40
  Output
8 1 1 7
3 1 4 7
5 3 2 1

2 2 1 2
4 2 1 2
6 2 1 2

3 10 3 10
9 10 3 10

# Note the last empty line, at the end of the output.
'''

def task02( L ):
    # your solution here
    pass

# ------------------------------------------------------------------------------

'''

Task 03

A **subarray** S of an array A is a slice of array A.
(The term subarray is more general then the term slice used 
mostly in scripting languages like Python, JavaScript and other.)
A subarray S of an array A is a **dense** subarray
when the sum of all elements in S is bigger or equal to
the half of the sum of all elements in A.

The task:
Find the shortest dense subarray S in input array A.  
Print three values: The indices of the first and the last item in S
and the sum of all items in S.
When there are more shortest dense subarrays in A, print the output
related only to the leftmost one. 
The entries on a line are separated by single spaces and the line contains no other symbols.

Example
  Input
3
3
1 0 2 0 0 0 3 4 0 1 1 2
1 3 5 7 9 2 4 6 8 10
0 0 0 39 0 41 0 
  Output
6 7 7
6 9 28
5 5 41   
'''

def task03( L ):
    # your solution here
    pass

# ------------------------------------------------------------------------------
'''
Task 04

An subarray S in array A array is loosely ascending 
when it contains at most one item which value is bigger then the value
of its immediate successor (to the right) in S.

The task:
In the given array A, find the longest loosely ascending subarray.
Print, on a separate line, the indices of the first and the last item in S. 
All values are to be printed on single line, separated by single spaces, 
and the line contains no other symbols.
If there are more than one longest loosely ascending subarrays of A, 
print the output related only to the leftmost one.
If there is no Loosely ascending subarray in A, print string 'None'.


Example 
  Input
4
1
12 10 8 6 4 2 1 3 7 8 9 11
  Output
5 11

'''

def task04( L ):
    # your solution here
    pass


# ------------------------------------------------------------------------------
# Task 05

'''
**Targets** and **shots** are points with integer coordinates on an infinite horizontal axis.
We are given a list of target coordinates and a list of shot coordinates.
A shot is a **hit** if the shot range contains at least half of the targets.
The shot is always exactly in the middle of the shot range, 
the width of the shot range is maximum possible but not bigger than half of the span of the targets. 
The span of the targets is one plus the distance from the leftmost
target to the rightmost target.
A target exactly at the border of the shot range is counted as contained in the shot range.
Shot quality is the number of targets in the shot range, if the shot is a hit.
Otherwise, shot quality is 0.

All coordinates are positive integers less than 10**6.
Both input lists, of targets and of shots, are sorted in ascending order.
There are no two targets with the same coordinate and no two shots with the same coordinate.
Note: A shot range may be located partially outside the range of targets,  
For example, its left border may be at negative index.


Example:
Symbols 'o' represent targets, symbols '*' represent shots.

          10       20        30        40        50        60
0123456789012345678901234567890123456789012345678901234567890   indexes
-----o-o---------oo---o---o--o------oo----------o---oo-------   targets
---*----*------*-------**------------*-----*--***------------   shots

There are 12 targets and 10 shots.  
The span of the targets is 1+53-5 = 49.
The width of the shot interval is 23.
(It cannot be 24 because then the shot could not be in its middle.)

Examples of some shots qualities:
          10       20        30        40        50        60
0123456789012345678901234567890123456789012345678901234567890   indexes
-----o-o----o--o-oo---o---o---------o-----------o---oo------- 
    |..........*..........| 8                                   Shot C range and quality 8
            |..........*..........| 6                           Shot D range and quality 6
             |..........*..........| 0                          Shot E range and quality 0
                                |..........*..........| 0       Shot G range and quality 0   
---*----*------*-------**------------*-----*--***------------   shots
   A    B      C       DE            F     G  HIJ

The task
Calculate the total of all shot qualities.
Print it on a separate line.
The coordinates of targets and shots are presented in the input in ascending order. 

Hint:
(It is a hint, not a cook-book recipe to follow mindlessly!)
Think how the function indexOfClosestBiggerValueTo() from the lectures,
based on binary search principle,
may be useful when applied to the list of targets and the left border of
a particular range. Would you need to apply similar reasoning
and appropriately modified binary search also to the right border
of the same range?
May prefix sum idea help somehow a bit?

Example
  Input
5
2
5 7 12 15 17 18 22 26 36 48 52 53
3 8 15 23 24 37 43 46 47 48
  Output
20
'''

def task05( targets, shots ):
    # your solution here
    pass

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int(input())
Nlists = int(input())
inputLists = []
for k in range(Nlists):
    oneList = list(map(int, input().split()))
    inputLists.append(oneList)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G

t1 = time.time()
if taskNo in [1, 2, 3, 4]:
    for aList in inputLists:
        if taskNo == 1:  task01(aList)
        if taskNo == 2:  task02(aList)
        if taskNo == 3:  task03(aList)
        if taskNo == 4:  task04(aList)
if taskNo == 5:
    for i in range(0, len(inputLists), 2):  # targets and shots
        task05(inputLists[i], inputLists[i + 1])

t2 = time.time()
# print( 'time', str(t2-t1)[:5] )

'''
Public data
The public data set is intended for easier debugging and approximate program correctness checking. The public data set is stored also in the upload system and each time a student submits a solution it is run on the public dataset and the program output to stdout and stderr is available to him/her.
Link to the public data set
'''
