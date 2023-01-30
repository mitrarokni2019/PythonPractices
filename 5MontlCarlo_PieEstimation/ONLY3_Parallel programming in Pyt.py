''' ONLY 1.3 Parallel programming in Python
"Mitra Rokni"
"mitra.rokni.0545@student.uu.se"
Reviewed by: Sergi Olives Juan
Date reviewed: 5/20/2022
'''

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from time import perf_counter as pc

def n_sphere_volume(iterations, dimension):
    no_inside = 0

    for _ in range(iterations):
        p = np.random.uniform(-1.0, +1.0, dimension)
        distance = np.linalg.norm(p)

        if distance <= 1.0:
            no_inside += 1
        
    return np.power(2.0, dimension) * (no_inside / iterations)

def run(processes,iterations, dimension ):
    start = pc()  # or we can use start = datetime.now()

    # iterations = int(input("iterations: "))
    # dimension = int(input("dimension: "))
    # processes = int(input("processes: "))

    batch_iterations = iterations // processes

    with ProcessPoolExecutor() as pool:
        result = pool.map(
            n_sphere_volume,
            [ batch_iterations ] * processes,
            [ dimension ] * processes
        )
    
    result = list(result)
    print("list of the results ",result)
    monte_result = reduce((lambda x, y: x + y), result)
    monte_final_results= monte_result/processes
    #print(monte_result)
    print("mean of the result's list", monte_final_results)
    end = pc() # or we can use end = datetime.now()

    elapsed_time = end - start
    print("<<  Elapsed time", elapsed_time,"   >>")


run(10, 1000000, 11)
run(10, 10000000,11)

