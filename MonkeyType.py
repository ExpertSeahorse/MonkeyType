import random
import string
import time

count = 0
match = False
strngbank = string.ascii_letters
strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
start = time.time()
while not match:
    ans = []
    for letter in range(len(strng)):
        a = random.choice(strngbank)
        ans.append(a)
    if "".join(ans) == strng:
        match = True
    elif count == 100000:
        break
    else:
        count += 1
print(count, "Tries")
print(time.time() - start, "Seconds")
