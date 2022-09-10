# %% 

import pandas as pd 
import numpy as np
import multiprocessing
import time
import random
from sklearn.datasets import make_classification
import os

output_files = 10

output_dir = 'files_to_process'

def generate_dataset(i):
    X,y = make_classification(n_samples=300000, n_features=15, n_informative=2, 
                        n_redundant=0, n_classes=2, n_clusters_per_class=2,
                            class_sep=0.5,
                    flip_y=0)
    
    y = pd.DataFrame(y,columns=['y'])
    X = pd.DataFrame(X)
    df = pd.concat([X,y],axis=1)
    
    file_name_to_write = f"my_csv_data_{i}.csv"

    print(f"Writing {file_name_to_write} to disk")
    # for i in range(4):
    df.to_csv(os.path.join(output_dir,file_name_to_write),index=False)



if __name__ == '__main__':    
    
    # ##-----------------------------------------------------------------##
    # ## Multiprocessing
        
    processs_array = []

    t1 = time.perf_counter()

    for i in range(10):
        p = multiprocessing.Process(target=generate_dataset, args=[i])
        processs_array.append(p)
        p.start()
        
                
    for p in processs_array:
        p.join()
        
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds') 
    
    