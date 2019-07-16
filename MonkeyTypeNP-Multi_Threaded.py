from string import ascii_letters
from time import time
from numpy import array, random
import os
from json import load, dump
from threading import Thread
from pathlib import Path
from shutil import rmtree
"""
By using numpy arrays to create the strings instead of a for loop,
the speed of the program is doubled
"""
# Set the file structure
folder = 'Auto_saves'
p = Path(folder)
p.mkdir(exist_ok=True)
auto_save = '_autosave.txt'
thread_put = 'thread_put.txt'


def logic_loop(strng, thread_num):
    t_auto_save = os.path.join(folder, str(thread_num) + auto_save)
    # If there is an autosave from an interrupted run:
    if os.path.exists(t_auto_save) and 'Finished' not in t_auto_save:
        with open(t_auto_save, 'r') as file:
            # Load the values from the save
            j_dict_in = load(file)
            count = j_dict_in['count']
            time_passed = j_dict_in['time_passed']

    # If the run finished, but others didnt...
    elif os.path.exists(t_auto_save) and 'Finished' in t_auto_save:
        # Abort the function
        return None

    else:
        # otherwise keep them to defaults
        count = 0
        time_passed = 0

    # Set default variables, the letter bank, and the answer string
    strngbank = array(list(ascii_letters))
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
            with open(t_auto_save, 'w') as file:
                dump(jdict, file)

    if os.path.exists(t_auto_save):
        with open(t_auto_save, 'a') as file:
            print("Finished", file=file)

    # Export the collected data into the thread output file
    with open(thread_put, 'a') as file:
        print(thread_num, count, time() - start + time_passed, file=file)

    # Returns count and the amount of time it took to complete the processing (For potential future programs)
    return count, time() - start + time_passed


if __name__ == '__main__':
    total_start = time()
    # Clears / Creates the output file to collect information from the threads
    with open(thread_put, 'w') as file:
        pass

    thread_list = []
    strng = 'abc'
    thread_ct = 10
    # str_wid = round(len(strng)/thread_ct)

    # for the desired # of threads...
    for i in range(1, thread_ct + 1):
        # Create a thread of the function logic_loop and pass the strng parameter
        # Need to pass str type parameters as len 1 tuples or else they are passed as an array of chars
        run_thread = Thread(target=logic_loop, args=(strng, i))
        # Add the thread to a list for later
        thread_list.append(run_thread)
        # Start the thread
        run_thread.start()

    print("All threads started")
    # For the threads in the list from before...
    for i, thread in enumerate(thread_list):
        # Wait until the next thread has finished (or continue immediately if it was faster than the prev one)
        thread.join()

    # within the output file...
    with open(thread_put, 'r') as file:
        # import the data
        fin = file.read()
        # split the lines into an array
        output = fin.split('\n')
        # extract the data out of each array
        for i, line in enumerate(output):
            output[i] = tuple(line.split(' '))
        # pop off a blank entry at the end
        output.pop()

    total_count = 0
    i = 1
    # Print the results of each of the threads
    for thr_num, ct, t in output:
        print('Trial #' + str(thr_num))
        print(ct, "Tries")
        print(t, "Seconds")
        total_count += int(ct)
        i += 1

    # Print the totals
    print("\nTotal:")
    print(total_count, "Tries")
    print(time() - total_start, "Seconds")

    # Removes the files at the end of the script
    rmtree(folder)
