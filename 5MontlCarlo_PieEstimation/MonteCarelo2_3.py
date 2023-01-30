'''  1.2 Approximate the volume of a d-dimensional hypersphere
    + 1.3 Parallel programming in Python
"Mitra Rokni"
"mitra.rokni.0545@student.uu.se"
Reviewed by: Sergi Olives Juan
Date reviewed: 5/20/2022
'''
   
import math
import numpy as np 
from time import perf_counter as pc
from functools import reduce
import concurrent.futures as future


'''
def hyper_exact(n,d):
  r=1
  v= math.pow((math.pi) ,(d/2)) * math.pow(r,d) / (math.gamma((d/2)+1))
  return v
'''
'''
def hyper_estimate(n, d):
    points_inside = 0

    for count_loops in range(n):
        points = np.random.uniform(-1.0, 1.0, d)
        distance = np.linalg.norm(points)
        if distance < 1.0:
            points_inside += 1

    return np.power(2.0, d) * points_inside / n
'''


hyper_exact = lambda n,d : math.pow((math.pi) ,\
    (d/2)) * math.pow(1,d) / (math.gamma((d/2)+1))



def hyper_estimate(n, d ):
  random_ponit_coordinates=[]
  n_inside=0
  n_outside=0
  for i in range (n):
    random_ponit_coordinates=[]
    random_ponit_coordinates = [np.random.uniform(-1,1) for _ in range(d)]
    #random_ponit_coordinates = [lambda x: x.np.random.uniform(-1,1) for x in range(d)]
    #for j in range (d):
      #x= np.random.uniform(-1,1)
      #random_ponit_coordinates.append(x)
    squares = map(lambda x: x * x, random_ponit_coordinates)
    distance = reduce((lambda x, y: x + y), squares)

    if distance <= 1:
      n_inside=n_inside+1
    else:
      n_outside= n_outside+1

  print(f"considering {n} points in {d}_D Space, there are {n_inside} points inside & {n_outside} outside of shape")
  estimated_v= math.pow(2, d)* n_inside / n
  return estimated_v
############################# Part 1: results printing  #########################################################
#print(f"for generating {n} points and {d}dimention, there are {n_inside} points inside  and {n_outside} outside ")
print("\n____________________ Part 2: final result is : ____________________________________\n")
print("estimated volume is :  ", hyper_estimate(100000,2))
print("actual volume b formula is :  ",hyper_exact(100000,2))
print("------------------------------------------------------------\n")
print("estimated volume is :  ",hyper_estimate (100000, 11))
print("actual volume b formula is :  ",hyper_exact (100000, 11) )
#print("------------------------------------------------------------\n")
#print("*estimated volume is :  ",hyper_estimate(100000,11))
#print("*actual volume formula is :  ",hyper_exact(10000000,11) )
#print("------------------------------------------------------------\n")
#print("*estimated volume is :  ",hyper_estimate(1000000,11))
#print("*actual volume formula is :  ",hyper_exact(1000000,11) )


############################# Part 2: execution time  #########################################################
print("\n____________________ Part 2: execution time : ____________________________________\n")

def RunningTime(n, d):   
        start = pc()
        hyper_estimate(n,d)
        end = pc()
        print("               << Process took {} seconds in python  >>".format(round(end-start, 4)))

        print("------------------------------------------------------------\n")

RunningTime(10000,2)
RunningTime(10000, 11)
print("*** ",RunningTime(1000000, 11))
print("*** ",RunningTime(10000000,11))
############################# Part 3: execution time  #########################################################
def parallel_processing_time(noProcesses, n,d):
    start = pc()
    result = []
    noProcesses=10
    division = int(n/noProcesses) # n points will be divided into shorter list or batch
    list_of_n = [division]*noProcesses
    
    list_of_dimensions = [d]*noProcesses
    
    
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(hyper_estimate,list_of_n,list_of_dimensions)
    
    end = pc()
    print("               << Elapsed time:",  end-start, "seconds")

print("\n____________________ PART3 :estimated time by applying parallel processing : _______________________________\n")

print("<<",parallel_processing_time(10, 1000,2),">>\n")
print("<<",parallel_processing_time(10, 1000,11),">>\n")
print("***\n<<", parallel_processing_time(10, 1000000, 11),">>\n")
print("***\n<<", parallel_processing_time(10, 10000000, 11,">>\n"))



