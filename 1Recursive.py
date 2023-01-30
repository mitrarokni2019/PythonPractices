#!/usr/bin/env python
# coding: utf-8
'''
Prcticing Recursion
Mitra Rokni
mitra.rokni88@gmail.com

'''

# ## 04: Calculate specific character in a given string


def CountChar(string, char):
    if not string:
        return 0
    else:
        return (string[0] == char) + CountChar(string[1:], char)


string = "jogging"
char = "j"
print(CountChar(string, char))





#4 second solution 
def findNr(s,ch, count=0):
    if s== '':
        return count
    else:
        if s[0]== ch:
            count = count+1
        return findNr(s[1:], ch , count )
        
        
s="my name is  mm mm mitra"
ch='m'
print(findNr(s,ch))


# ## 05: Power of

def Pow(n, m):
    if (m == 0):
        return 1
    else:
        return n * Pow(n, m-1)   

n, m = 2, 5
print(Pow(n, m))


# ## 06: Multiplication of integers

def Mul(n, m):
    if (m == 0):
        return 0
    elif (m == 1):
        return n
    else:
        return n + Mul(n, m-1)

n, m = 2, 5
print(Mul(n, m))


# ## 08: Harmonic sum

def Harmonic(n):
    if (n == 1):
        return 1
    else:
        return (1 / n) + Harmonic(n-1)

n = 2
print(Harmonic(n))


# ## 09: Largest value in a list

# first 
def Large(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] if list[0] > Large(list[1:]) else Large(list[1:])
    
list = [1, 2, 3, 4, 5]
print(Large(list))    


#9 second way:
def large_value(list):
    if len(list) == 1:
        return list[0]
    else:
        big = large_value(list[1:])
        if list[0] > big:
            return list[0]
        else:
            return big

        
list = [2,44,5,0]
print(large_value(list))


# ## 10: Reverse order

def Reverse(string):
    if not string:
        return ""
    else:
        return string[-1] + Reverse(string[:-1])


string = "sample string"
print(Reverse(string))


# ## 14: Matching parentheses

def Match(string, counter = 0):
    if not string:
        return (counter == 0)
    if (counter > 0):
        return False
    if string[-1] == ")":
        return Match(string[:-1], counter-1)
    elif string[-1] == "(":
        return Match(string[:-1], counter+1)
    else:
        return Match(string[:-1], counter)

string = "((((()))))"
print(Match(string))

string = "(()))))"
print(Match(string))


def Match(string):
    s = Stack()
    balanced = True
    index = 0
    if not string:
        return list
    if (stack= 0):
        return False
    if string[-1] ==`````````````````````````````````````` ")":
        return Match(string[:-1], counter-1)
    elif string[-1] == "(":
        return Match(string[:-1], counter+1)
    else:
        return Match(string[:-1], counter)


# ## 15 : Algorithm Analysis tasks

# 03: Time to calculate Fibonacci sequence
import time
def fib(n):
    if n in (0,1) :
        return n 
    else: 
        return fib(n-1)+fib(n-2)
time.time()


# 03: Time to calculate Fibonacci sequence

def fib(n):
    if n in (0,1) :
        return n 
    else: 
        return fib(n-1)+fib(n-2)

print(fib(35))

# with watch      8.093= c* 1.618^35


print(pow(1.618,35))
print(8.093/20618074.50599988)


# t(50)= 545081.062694147 * 1.618^50
#t(100)= 545081.062694147* 1.618^100
n=1.618 
m=50
m=100
print(pow(n,m)* 545081.062694147)
m=100
print(pow(n,m)*545081.062694147)


#05: Insertion sort
def sortIns(l,n):
    if(n>1):
        sortIns(1,n-1)
        x= 1[n-1]
        i=n-2
        while(i>=0 and l[i]<x):
            l[i+1]=l[i]
            i=i-1
        l[i+1]=x
    
n=5
l=[2,7,4,5,61,22,34]
# the answer of this book is in the word-version file


# 06: Compare insertion and merge sort
# the answer of this book is in the word-version file

