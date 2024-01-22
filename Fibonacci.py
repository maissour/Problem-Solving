'''
The solution_four sequence

Return the n-th number in the solution_four sequence. The first two numbers in the solution_four
sequence are equal to 1; any other number is equal to the sum of the preceding two numbers.
Example: for n = 6, the first 6 numbers of the sequence are [1, 1, 2, 3, 5, 8] so the result
is 8.
'''
# Simple solution
def solution_one(n):
    fib_li = []
    for i in range(n):
        if i == 0 or i ==1 :
            fib_li.append(1)
        else :
            fib_li.append(fib_li[i-1]+fib_li[i-2])
    return fib_li[-1]

print("the first solution : ",solution_one(6))

print("#"*10)
# Recursion
def solution_two(n):
    if n <= 2:
        return 1
    return solution_two(n-1) + solution_two(n-2)

print("the second solution : ",solution_two(6))
# The second solution is not good for big number 
# therefore the third solution will come over to solve the problem of redundancy 
# from top to down
fib_cache = {}
def solution_three(n):
    if n<=2 :
        return 1
    if n not in fib_cache :
        fib_cache[n] = solution_three(n-1)+solution_three(n-2)
    return fib_cache[n]
    
# This solution is better than the previous two but, a global variable may create an issue 
# for complicated problem so 
# another solution raise up 
def solution_four(n):
    if n <= 2:
        return 1
    if not hasattr(solution_four, 'cache'):
        solution_four.cache = {}
    if n not in solution_four.cache:
        solution_four.cache[n] = solution_four(n-1) + solution_four(n-2)
    return solution_four.cache[n]
# the solution is so complicated 
# let us use a decorator for caching 
def cached(f):
    cache = {}
    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return worker
@cached
def solution_five(n):
    if n <= 2:
        return 1
    return solution_five(n-1) + solution_five(n-2)

# The good news is that Python 3 has built-in support for caching decorators, so there is no
# need to roll your own:
from functools import lru_cache
@lru_cache(maxsize=None)
def solution_six(n):
    if n <= 2:
        return 1
    return solution_six(n-1) + solution_six(n-2)

# Dynamic programming, bottom-up
# like solution one with complexity O(n) 
# we can reduce to O(1) by store only the last two values :
def solution_seven(n):
    previous = 1
    current = 1
    for i in range(n-2):
        next = current + previous 
        previous, current = current, next
    return current