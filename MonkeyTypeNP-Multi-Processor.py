from string import ascii_letters
from time import time
from numpy import array, random
from os import path, remove, cpu_count
from json import load, dump
import multiprocessing as mp
"""
By using numpy arrays to create the strings instead of a for loop,
the speed of the program is doubled
"""
# Set the file names
auto_save = 'autosave.txt'
process_put = 'process_put.txt'


def logic_loop(strng, process_num):
    t_auto_save = str(process_num) + auto_save
    # If there is an autosave from an interrupted run:
    if path.exists(t_auto_save):
        with open(t_auto_save, 'r') as file:
            # Load the values from the save
            j_dict_in = load(file)
            count = j_dict_in['count']
            time_passed = j_dict_in['time_passed']
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

    # Export the collected data into the process output file
    with open(process_put, 'a') as file:
        print("Thread#" + str(process_num) + ":", count, time() - start + time_passed, file=file)

    # After the test is over, if there is an autosave file, delete it
    if path.exists(t_auto_save):
        remove(t_auto_save)

    # Returns count and the amount of time it took to complete the processing
    return count, time() - start + time_passed


if __name__ == '__main__':
    total_start = time()
    # Clears / Creates the output file to collect information from the processes
    with open(process_put, 'w') as file:
        pass

    process_list = []
    strng = 'abc'
    process_ct = cpu_count()
    # str_wid = round(len(strng)/process_ct)

    # for the desired # of processes...
    for i in range(1, process_ct + 1):
        # Create a process of the function logic_loop and pass the strng parameter
        # Need to pass str type parameters as len 1 tuples or else they are passed as an array of chars
        run_process = mp.Process(target=logic_loop, args=(strng, i))
        # Add the process to a list for later
        process_list.append(run_process)
        # Start the process
        run_process.start()

    print("All Processes Running")
    # For the processes in the list from before...
    for i, process in enumerate(process_list):
        # Wait until the next process has finished (or continue immediately if it was faster than the prev one)
        process.join()

    # within the output file...
    with open(process_put, 'r') as file:
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
    # Print the results of each of the processes
    print()
    for p, ct, t in output:
        print(p)
        print(ct, "Tries")
        print(round(float(t), 3), "Seconds")
        total_count += int(ct)
        print()

    # Print the totals
    print("\nTotal:")
    print(total_count, "Tries")
    print(round(time() - total_start, 3), "Seconds")

    # Removes the file at the end of the script
    remove(process_put)
