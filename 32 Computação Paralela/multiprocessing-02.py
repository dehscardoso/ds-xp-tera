
# %% 

import pandas as pd 
import numpy as np
import multiprocessing 
import time
import os
import glob
from sklearn.neural_network import MLPClassifier

input_dir = 'files_to_process'
output_dir = 'files_processed'

files_to_process = glob.glob(os.path.join(input_dir,"*.csv"))


def load_file_and_train_model(file_dir):
    
    print(f"Reanding and processing {file_dir}")
    
    file_name = os.path.basename(file_dir)
    
    t1 = time.perf_counter()
    df = pd.read_csv(file_dir)
    t2 = time.perf_counter()
    
    print(f'Finished reading in {t2-t1} seconds') 
    
    
    t1 = time.perf_counter()
    df['new_column'] = df.apply(lambda row: (np.power(row[2],3)+np.sqrt(np.power(row[3],2)))/np.sqrt(np.power(row[5],4)))
    t2 = time.perf_counter()
    print(f'Finished processing in {t2-t1} seconds') 

    
    t1 = time.perf_counter()
    df.to_csv(os.path.join(output_dir,file_name))    
    t2 = time.perf_counter()
    print(f'Finished writing in {t2-t1} seconds') 
    
    
    


if __name__ == '__main__':    
    
    ##-----------------------------------------------------------------##
    # Single process 

    # t1 = time.perf_counter()
    # for i in tqdm(files_to_process):
    #     load_and_transform_data(i)
    # t2 = time.perf_counter()
    # print(f'Finished in {t2-t1} seconds') 
    
   
    # ##-----------------------------------------------------------------##
    # ## Multiprocessing
        
    processs_array = []

    t1 = time.perf_counter()

    for file_dir in files_to_process:
        p = multiprocessing.Process(target=load_and_transform_data, args=[file_dir])
        processs_array.append(p)
        p.start()
        
                
    for p in processs_array:
        p.join()
        
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds') 
    
    