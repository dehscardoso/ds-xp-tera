
# %% 

import pandas as pd 
import numpy as np
import threading
import multiprocessing 
import time
import random
from sklearn.datasets import make_classification
import requests
import os
import glob
from tqdm import tqdm
input_dir = 'files_to_process'
output_dir = 'files_processed'


ranges_to_calculate = [100_000_000,200_000_000,300_000_000]


def sum_square(x: int) -> int:
  final = 0
  for i in range(x):
    final += i * i
  return final

    
    
    
        
##-----------------------------------------------------------------##
## Single thread 

# t1 = time.perf_counter()

# for r in ranges_to_calculate:
#     sum_square(r)
    
# t2 = time.perf_counter()

# print(f'Finished in {t2-t1} seconds') 


##-----------------------------------------------------------------##
## Multithreading
     

threads_array = []

t1 = time.perf_counter()

for r in ranges_to_calculate:
    t = threading.Thread(target=sum_square, args=[r])
    threads_array.append(t)
    t.start()
    
            
print(f'Active Threads: {threading.active_count()}')
        
for t in threads_array:
    t.join()
    
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds') 



