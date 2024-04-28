'''
M06 Programing Assignment 15.1
April 27, 2024
Taylor Hickman
'''

import multiprocessing
import time
import random
from datetime import datetime

def clock():
#generate a random time between 0 and 1 second
    clock_time = random.random()
    time.clock(clock_time)
    
#current time
    current_time = datetime.now().strftime("%H:%M:%S")
    
    print(f"Process {multiprocessing.current_process().name} Current time: {current_time}")
    
if __name__ == '__main__':
# 3 processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=clock, name=f"Process-{i+1}")
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()