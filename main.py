import numpy as np
from operations import *
import time

lst = [9,10,11,13]
target = 24

start_time = time.time()
result = solver(lst,target)
if result == []:
    print("No Solution with target",target,"given", lst)
else:
    print("Total of",len(result), "solutions")
print(time.time()-start_time)




