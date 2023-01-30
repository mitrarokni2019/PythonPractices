''' # My  Code#
Comparing exacution time of Fib Function in Python vs C++

"mitra rokni"
Mail:"mitra.rokni.0545@student.uu.se"
'''


#!/usr/bin/env python3.9

import time
from time import perf_counter as pc
from time import sleep as pause
import matplotlib.pyplot as plt
from integer import Integer
from numba import njit

def fib_py(n):
    if n in (0,1) :
        return n
    else:
        return fib_py(n-1)+fib_py(n-2)

@njit
def fib_numba(n):
    if n in (0,1) :
        return n
    else:
        return fib_numba(n-1)+fib_numba(n-2)

if __name__ == "__main__":
    lst_i_c=[]
    lst_time_c=[]
    for i in range(35,45):
        lst_i_c.append(i)
        start = pc()
        f=Integer(i)
        f.fib()
        end = pc()
        lst_time_c.append(round(end-start, 4))
        print("Process took {} seconds in C++ for i  {}".format(round(end-start, 4),i))

if __name__ == "__main__":
    lst_i_p=[]
    lst_time_p=[]
    for i in range(35,45):
        lst_i_p.append(i)
        start = pc()
        fib_py(i)
        end = pc()
        lst_time_p.append(round(end-start, 4))
        print("Process took {} seconds in python for i  {}".format(round(end-start, 4),i))

if __name__ == "__main__":
    lst_i_numba=[]
    lst_time_numba=[]
    for i in range(35,45):
        lst_i_numba.append(i)
        start=pc()
        fib_numba(i)
        end = pc()
        lst_time_numba.append(round(end-start, 4))
        print("Process took {} seconds in numba for i  {}".format(round(end-start, 4),i))

plt.plot(lst_i_c,lst_time_c, color='r', label="by C++")
plt.plot(lst_i_p,lst_time_p,color='g',label="by python")
plt.plot(lst_i_numba,lst_time_numba,color='b',label="by numba")
plt.title("the amount of time  Python Vs C++ Vs Numba")
plt.ylabel('time')
plt.xlabel("iterations")
plt.legend(loc='upper left')
plt.savefig("PlottingExecutionTime.png")

if __name__ == "__main__":
	f=Integer(47)
	print("fib 37 by numba is equal to :",fib_py(47) )
	print("fib 37 by python is equal to :",fib_numba(47) )
	print("fib 37 by c++ is equal to :", f.fib() )
