from random import choice
from string import ascii_letters
from time import time
from threading import Thread
"""
This is an exploration of how threading can be used to shorten operation time
"""


def logic_loop(strng):
    # Set the variables to their defaults
    count = 0
    start = time()
    match = False
    # Set the total answer bank of letters and the arrangement we are looking for
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

    with open(filename, 'a') as file:
        print(count, time()-start, file=file)


if __name__ == '__main__':
    total_start = time()
    filename = 'output.txt'
    # Clears / Creates the output file to collect information from the threads
    with open(filename, 'w') as file:
        pass

    thread_list = []
    strng = 'AbCdEFghiJkLmnopqRSTu'
    thread_ct = 10
    # str_wid = round(len(strng)/thread_ct)

    # for the desired # of threads...
    for i in range(1, thread_ct + 1):
        # Create a thread of the function logic_loop and pass the strng parameter
        # Need to pass str type parameters as len 1 tuples or else they are passed as an array of chars
        run_thread = Thread(target=logic_loop, args=(strng,))
        # Add the thread to a list for later
        thread_list.append(run_thread)
        # Start the thread
        run_thread.start()

    # For the threads in the list from before...
    for i, thread in enumerate(thread_list):
        # Wait until the next thread has finished (or continue immediately if it was faster than the prev one)
        thread.join()
        # Print that it's done
        print("Thread #", i + 1, "is done")

    # within the output file...
    with open(filename, 'r') as file:
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
    for ct, t in output:
        print('Trial #' + str(i))
        print(ct, "Tries")
        print(t, "Seconds")
        total_count += int(ct)
        i += 1

    # Print the totals
    print("\nTotal:")
    print(total_count, "Tries")
    print(time() - total_start, "Seconds")
