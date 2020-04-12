import numpy as np
from operations import *
import time

lst = [9,12,12,10]
target = 24

start_time = time.time()
result = solver(lst,target)
if result == []:
    print("No Solution with target",target,"given", lst)
else:
    print("Total of",len(result), "solutions")
print(time.time()-start_time)

print("DONE")
# print(cartProd([2,3,1],repeat = 2))





