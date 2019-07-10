from time import time
from string import ascii_letters
from numpy import random, array
from statistics import mean, pstdev
from json import load, dump
from os import path, remove
"""
Finds the avg time/tries the script will need to match the answer

Use the auto_save files created to monitor progress in the program
"""
# Sets file names for saving
trial = 'trial_save.txt'
auto_save = "auto_save.txt"

# If there is a trial save file in the folder(if there was an interrupted run)...
if path.exists(trial):
    with open(trial, 'r') as file:
        # Load the JSON from the file and reset the variables
        t_dict_in = load(file)
        done = t_dict_in['trial']
        avg_ct = t_dict_in['avg_count']
        avg_time = t_dict_in['avg_time']
else:
    # Otherwise, the variables are blank
    done = 0
    avg_ct = []
    avg_time = []

# Set the answer bank and the key
strngbank = array(list(ascii_letters))
target_str = "ABC"

# Over the number of trials...
for i in range(done, 10):
    # If there is an auto_save from an interrupted run:
    if path.exists(auto_save):
        with open(auto_save, 'r') as file:
            # Load the values from the save
            a_dict_in = load(file)
            count = a_dict_in['count']-1
            old_time = a_dict_in['passed_time']
            start = time()
    else:
        # otherwise keep them to defaults
        count = 0
        start = time()
        old_time = 0

    # until a match is made...
    match = False
    while not match:
        # make a random selection of letters from the answer bank...
        # using numpy.random.choice to choose the characters is 2x faster than using a for loop
        ans = random.choice(strngbank, size=len(target_str))

        # And if those letters are the same as the key...
        if "".join(ans) == target_str:
            # break the loop.
            match = True
        else:
            # Otherwise add one to the counter
            count += 1

        # And if the counter hits 1 million...
        if count % 1000000 == 0:
            # Compile a save file of the necessary data
            a_dict = {'count': count,
                      'passed_time': time() - start + old_time}

            with open(auto_save, 'w') as file:
                # And dump it into a JSON
                dump(a_dict, file)

    # After a match is made, add the count total to an array and add the delta time to another array
    avg_ct.append(count)
    avg_time.append(time() - start + old_time)

    # And back it up
    with open(trial, 'w') as file:
        t_dict = {'trial': i+1,
                  'avg_count': avg_ct,
                  'avg_time': avg_time}
        dump(t_dict, file)

    # If there is an auto_save, delete it so it wont interrupt the next run
    if path.exists(auto_save):
        remove(auto_save)

# After the program finishes, delete the trial backup
if path.exists(trial):
    remove(trial)

# Find the averages number of attempts and the average time
mct = mean(avg_ct)
mt = mean(avg_time)
std_ct = pstdev(avg_ct)
std_t = pstdev(avg_time)
print("On average:", mct, "tries, with a standard deviation of:", std_ct)
print("On average:", mt, "Seconds, with a standard deviation of:", std_t)
