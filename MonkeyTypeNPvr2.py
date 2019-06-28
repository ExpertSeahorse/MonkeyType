import time
import string
import numpy as np
from statistics import *
import json
import os
# TODO: Add trialsave.txt with trial information (i, arrays)
"""
Finds the avg time/tries the script will need to match the answer
"""

strngbank = np.array(list(string.ascii_letters))
target_str = "ABCd"
avg_ct = []
avg_time = []
if os.path.exists("autosave.txt"):
    with open('autosave.txt', 'r') as file:
        jdictin = json.load(file)
        done = jdictin['trial']
else:
    done = 0
for i in range(done, 10):
    if os.path.exists("autosave.txt"):
        with open('autosave.txt', 'r') as file:
            jdictin = json.load(file)
            count = jdictin['count']
            old_time = jdictin['passed_time']
            start = time.time()
    else:
        count = 0
        start = time.time()
        old_time = 0

    match = False
    while not match:
        ans = np.random.choice(strngbank, size=len(target_str))
        if "".join(ans) == target_str:
            match = True
        else:
            count += 1
        if count % 1000000 == 0:
            jdict = {'count': count,
                     'passed_time': time.time() - start + old_time,
                     'trial': i}
            with open('autosave.txt', 'w') as file:
                json.dump(jdict, file)

    avg_ct.append(count)
    avg_time.append(time.time() - start + old_time)
    if os.path.exists("autosave.txt"):
        os.remove("autosave.txt")

mct = mean(avg_ct)
mt = mean(avg_time)
print(avg_ct, avg_time)
print("On average:", mct, "tries")
print("On average:", mt, "Seconds")
