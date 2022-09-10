
# %% 

import pandas as pd 
import numpy as np
import threading
import time
import random
from sklearn.datasets import make_classification
import requests
import os

urls_to_download = [
    'https://picsum.photos/seed/1/1920/1080',
    'https://picsum.photos/seed/2/1920/1080',
    'https://picsum.photos/seed/3/1920/1080',
    'https://picsum.photos/seed/4/1920/1080',
    'https://picsum.photos/seed/5/1920/1080',
    'https://picsum.photos/seed/6/1920/1080',
    'https://picsum.photos/seed/7/1920/1080',
    'https://picsum.photos/seed/8/1920/1080',
    'https://picsum.photos/seed/9/1920/1080',
    'https://picsum.photos/seed/10/1920/1080',
    'https://picsum.photos/seed/11/1920/1080',
    'https://picsum.photos/seed/12/1920/1080',
    'https://picsum.photos/seed/13/1920/1080',
    'https://picsum.photos/seed/14/1920/1080',
    'https://picsum.photos/seed/15/1920/1080',
    'https://picsum.photos/seed/16/1920/1080',
    'https://picsum.photos/seed/17/1920/1080'
]



output_dir = 'downloaded_images'

## 

def download(url):
    print(f'downloading {url}')
    img_data = requests.get(url).content
    img_name = url.split('/')[-3]
    img_name = f'{img_name}.jpg'
    print(f'Received data for {img_name}')
    with open(os.path.join(output_dir,img_name), 'wb') as img_file:
        img_file.write(img_data)
        
        

            
        
##-----------------------------------------------------------------##
## Single thread 

t1 = time.perf_counter()
for i in urls_to_download:
    download(i)
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds') 


##-----------------------------------------------------------------##
## Multithreading
     

threads_array = []

t1 = time.perf_counter()

for url in urls_to_download:
    t = threading.Thread(target=download, args=[url])
    threads_array.append(t)
    t.start()
    
            
print(f'Active Threads: {threading.active_count()}')
        
for t in threads_array:
    t.join()
    
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds') 



##-----------------------------------------------------------------##
## Variando o numero de threads 


# def download_list(idx,urls_list):
#     print(f'Thread {idx} focused on list {urls_list}')
#     for url in urls_list:
#         img_data = requests.get(url).content
#         img_name = url.split('/')[4]
#         img_name = f'{img_name}.jpg'
#         print(f'downloading {img_name}')
#         with open(os.path.join(output_dir,img_name), 'wb') as img_file:
#             img_file.write(img_data)

# def chunks(lst,n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]


# for thread_count in [3]:

#     t1 = time.perf_counter()

#     threads_array = []
    
#     itens_per_thread = int(len(urls_to_download)/thread_count)


#     for i in range(thread_count):
#         list_per_thread = list(chunks(urls_to_download,itens_per_thread))[i]
#         t = threading.Thread(target=download_list, args=[i,list_per_thread])
#         threads_array.append(t)
#         t.start()
                
#     print(f'Active Threads: {threading.active_count()}')

            
#     for t in threads_array:
#         t.join()

#     t2 = time.perf_counter()
#     print(f'Finished in {t2-t1} seconds') 