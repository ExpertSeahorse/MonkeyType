from string import ascii_letters
from time import time
from numpy import array, random
from os import path, remove
from json import load, dump
"""
By using numpy arrays to create the strings instead of a for loop,
the speed of the program is doubled
"""
# Set the autosave file name
auto_save = 'autosave.txt'

# If there is an autosave from an interrupted run:
if path.exists(auto_save):
    with open(auto_save, 'r') as file:
        # Load the values from the save
        jdict_in = load(file)
        count = jdict_in['count']
        time_passed = jdict_in['time_passed']
else:
    # otherwise keep them to defaults
    count = 0
    time_passed = 0

# Set default variables, the letter bank, and the answer string
strngbank = array(list(ascii_letters))
strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
start = time()
match = False
# While there is no match...
while not match:
    # Make a random string with numpy's random.choice
    ans = random.choice(strngbank, size=len(strng))

    # if that random string matches the answer key, break the loop
    if "".join(ans) == strng:
        match = True
    # Otherwise add one to count
    else:
        count += 1
    # If count hits 1 million, 2 million, ...
    if count % 1000000 == 0:
        # save the count number and time passed
        jdict = {'count': count,
                 'time_passed': time()-start}
        with open(auto_save, 'w') as file:
            dump(jdict, file)

# After the test is over, if there is an autosave file, delete it
if path.exists(auto_save):
    remove(auto_save)

# Print the results
print(count, "Tries")
print(time() - start + time_passed, "Seconds")
