from random import choice
from string import ascii_letters
from time import time
"""
This is a legacy version of MonkeyType, this program has been recreated using numpy arrays in MonkeyTypeNP
"""
# Set the variables to their defaults
count = 0
match = False
start = time()

# Set the total answer bank of letters and the arrangement we are looking for
strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Until there is a match...
while not match:
    ans = []
    # For the total length of the string...
    for letter in range(len(strng)):
        # choose a random letter from the bank and add it to the possible answer
        a = choice(ascii_letters)
        ans.append(a)

    # If the random letters match the answer string...
    if "".join(ans) == strng:
        # break the loop
        match = True
    else:
        # Otherwise, add one to count
        count += 1
    # If count is 1 million...
    if count == 1000000:
        # break out of the loop
        # This is used to find the time is takes to hit 1 million tries,
        # otherwise I'd put an output statement here to ensure the program is working
        match = True
        break

# Print the results of the test
print(count, "Tries")
print(time() - start, "Seconds")
