
# %% 

import pandas as pd 
import numpy as np
import threading
import time
import random

global global_counter
global_counter = 0

## 
def my_wait_function(idx,seconds):
    
    global global_counter
    global_counter = global_counter+1
    
    print(f'Global variable is {global_counter}')
    print(f'Starting thread {idx} | Waiting for {seconds:0.2f} second(s) | Global counter {global_counter}', end = "\n")
    time.sleep(seconds)
    print(f'Done Waiting {seconds:0.2f}  second(s)')
     

##-----------------------------------------------------------------##
## Single thread 

wait_time = random.uniform(0,1)
my_wait_function(0,wait_time)


##-----------------------------------------------------------------##
## Multithreading
     

number_of_threads = 5

threads_array = []

for i in range(number_of_threads):
    wait_time = random.uniform(0,1)
    t = threading.Thread(target=my_wait_function, args=[i,wait_time])
    threads_array.append(t)
    t.start()
            
print(f'Active Threads: {threading.active_count()}')

        
for t in threads_array:
    t.join()
    

