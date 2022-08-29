def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    list_range = range(start, stop+1)
    for item in list_range:
        print(item)


count_up(5, 7)        
