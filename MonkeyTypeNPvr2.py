import time
import string
import numpy as np
from statistics import *

"""
Finds the avg time/tries the script will need to match the answer
"""

match = False
strngbank = np.array(list(string.ascii_letters).extend(".,!? \'\""))
target_str = "ABCde"
avg_ct = []
avg_time = []

for i in range(30):
    count = 0
    start = time.time()
    while not match:
        ans = np.random.choice(strngbank, size=len(target_str))
        if "".join(ans) == target_str:
            match = True
        else:
            count += 1
    avg_ct.append(count)
    avg_time.append(time.time() - start)

mct = mean(avg_ct)
mt = mean(avg_time)
print("On average:", mct, "tries")
print("On average:", mt, "Seconds")
