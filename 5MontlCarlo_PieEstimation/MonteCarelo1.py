""" 1.1 Monte Carlo approximation of π
"Mitra Rokni"
"mitra.rokni.0545@student.uu.se"
Reviewed by: Sergi Olives Juan
Date reviewed: 5/20/2022
"""
# part 1.1
import numpy as np 
import matplotlib.pyplot as plt
import math 

'''figure, axes = plt.subplots()
Drawing_uncolored_circle= plt.Circle( (0, 0 ), 1 , color='yellow', fill = False )
axes.set_aspect( 1 )
axes.add_artist( Drawing_uncolored_circle )
plt.show()'''

numb=[1000,10000,100000]
n_inside=0  # number of points inside of circle
n_outside=0   # number of points outside of circle
pi_estimated=[]  # list of approximated pi for each element of list numb
nx_inside=[]   #  list of Xs of points which are inside of circle
fnx_inside=[]  #  list of Ys of points which are inside of circle
nx_outside=[]   #  list of Xs of points which are outside of circle
fnx_outside=[]  #  list of Ys of points which are outside of circle

for count in range (len(numb)):
    for i in range (numb[count]):
        n= np.random.uniform(-1,1)   # generating random point  (for X-axis)
        fn= np.random.uniform(-1,1)  # generating random point  (for Y-axis)
        
        if (n**2+fn**2)<=1:
            n_inside=n_inside+1
            fnx_inside.append(n) 
            nx_inside.append(fn)
            
        else:
            n_outside=n_outside+1
            fnx_outside.append(n)
            nx_outside.append(fn)
    p= (4* n_inside)/numb[count]
    pi_estimated.append(p)
    plt.scatter(nx_inside,fnx_inside,color='red')
    plt.scatter(nx_outside,fnx_outside, color='blue')
    plt.title(f'for N = {numb[count]}\n estimated pi={p} & actual pi={math.pi}')
    plt.show()
            
    print(f"with generating {numb[count]} points, there are {n_inside} points inside of circle and {n_outside} outside of circle")
    #p= (4* n_inside)/numb[count]
    #pi_estimated.append(p)
    print("               estimated pi  = ", p )
    print("               actual pi with python math packageis = ", math.pi)
    
       

print("\n  ************** In conclusion *************")
print("pi which are estimated for n= 1000,10000,100000 are:  ", pi_estimated)
print("real pi with python math package is: ", math.pi)




