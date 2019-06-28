import string
import time
import numpy as np
import json
"""
By using numpy arrays to create the strings instead of a for loop,
the speed of the program is doubled
"""
count = 0
match = False
strngbank = np.array(list(string.ascii_letters))
strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
start = time.time()
while not match:
    ans = np.random.choice(strngbank, size=len(strng))
    if "".join(ans) == strng:
        match = True
    else:
        count += 1
    if count % 1000000 == 0:
        jdict = {'count': count}
        json.dump()
print(count, "Tries")
print(time.time() - start, "Seconds")
