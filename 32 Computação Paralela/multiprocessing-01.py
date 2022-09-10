
# %% 

import pandas as pd 
import numpy as np
import threading
import multiprocessing 
import time
from sklearn.datasets import make_classification
input_dir = 'files_to_process'
output_dir = 'files_processed'


ranges_to_calculate = [100_000_000,150_000_000,200_000_000,250_000_000,300_000_000]


def sum_square(x: int) -> int:
  final = 0
  for i in range(x):
    final += i * i
  return final

    
    
##-----------------------------------------------------------------##
## Single process 

# t1 = time.perf_counter()

# for r in ranges_to_calculate:
#     sum_square(r)
    
# t2 = time.perf_counter()

# print(f'Finished in {t2-t1} seconds') 

    
  


if __name__ == '__main__':    
  

  ##-----------------------------------------------------------------##
  ## Multiprocessing
        
  process_array = []

  t1 = time.perf_counter()

  for r in ranges_to_calculate:
      p = multiprocessing.Process(target=sum_square, args=[r])
      process_array.append(p)
      p.start()
      
              
  for p in process_array:
      p.join()
      
  t2 = time.perf_counter()
  print(f'Finished in {t2-t1} seconds') 
  
  


