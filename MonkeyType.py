import random
import string
import time
"""
This is a legacy version of MonkeyType, this program has been recreated using numpy arrays in MonkeyTypeNP
"""
# Set the variables to their defaults
count = 0
match = False
start = time.time()

# Set the total answer bank of letters and the arrangement we are looking for
strngbank = string.ascii_letters
strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Until there is a match...
while not match:
    ans = []
    # For the total length of the string...
    for letter in range(len(strng)):
        # choose a random letter from the bank and add it to the possible answer
        a = random.choice(strngbank)
        ans.append(a)

    # If the random letters match the answer string...
    if "".join(ans) == strng:
        # break the loop
        match = True
    else:
        # Otherwise, add one to count
        count += 1
    # If count is 1 million...
    if count == 100000:
        # break out of the loop
        # This is used to find the time is takes to hit 1 million tries,
        # otherwise I'd put a print statement here to ensure the program is working
        break

# Print the results of the test
print(count, "Tries")
print(time.time() - start, "Seconds")
