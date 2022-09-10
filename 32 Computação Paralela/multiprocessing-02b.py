
# %% 

import pandas as pd 
import numpy as np
import multiprocessing 
import time
import os
import glob
import tqdm
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

input_dir = 'files_to_process'

files_to_process = glob.glob(os.path.join(input_dir,"*.csv"))


def load_file_and_train_model(model_index,file_dir):
    
    print(f"Reanding and processing {file_dir}")
    file_name = os.path.basename(file_dir)
    
    t1 = time.perf_counter()
    df = pd.read_csv(file_dir)
    t2 = time.perf_counter()
    print(f'Finished reading in {t2-t1} seconds') 
    
    ##----------------------
    t1 = time.perf_counter()
    
    clf = MLPClassifier(solver='adam',hidden_layer_sizes=(15, 2))
    
    y = df['y']
    X = df[[c for c in df.columns if 'y' not in c]]
    
    X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.33, random_state=42)
    
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    
    t2 = time.perf_counter()
    print(f"Accuracy of model {model_index} is {acc:0.2f} | Finished training in {t2-t1} seconds")

  
    


if __name__ == '__main__':    
    
    ##-----------------------------------------------------------------##
    # Single process 

    # t1 = time.perf_counter()
    # for file in tqdm.tqdm(files_to_process):
    #     load_file_and_train_model(0,file)
    # t2 = time.perf_counter()
    # print(f'Finished in {t2-t1} seconds') 
    
   
    # ##-----------------------------------------------------------------##
    ## Multiprocessing
        
    processs_array = []

    t1 = time.perf_counter()

    for i,file_dir in enumerate(files_to_process):
        p = multiprocessing.Process(target=load_file_and_train_model, args=[i,file_dir])
        processs_array.append(p)
        p.start()
        
                
    for p in processs_array:
        p.join()
        
    t2 = time.perf_counter()
    print(f'Finished the whole training in {t2-t1} seconds') 

    
    