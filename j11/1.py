def miangin(a: float, b: float, c: float, d: float)-> float:
    """
    Calculates the average of 4 scores and assigns a grade based on the average.

    Args:
        a (float): Score 1
        b (float): Score 2
        c (float): Score 3
        d (float): Score 4

    Returns:
        float: The average of the 4 scores
    """
    # List of valid scores
    valid = range(0, 21)
    # List of scores
    lst = [a, b, c, d]
    # List of valid scores
    valid_lst = []
    # Iterate over the scores
    for i in lst:
        # Check if the score is valid
        if i in valid:
            # Add the score to the list of valid scores
            valid_lst.append(i)
    # Calculate the average
    avg= sum(valid_lst)/len(valid_lst)

    # Assign a grade based on the average
    if  avg >=16:
        print(avg, "A")
    elif  avg >=14:
        print(avg, "B")
    elif  avg >=12:
        print(avg, "C")
    elif  avg >=10:
        print(avg, "D")
    else:
        print("Faild")
    
miangin(10, 25, 15, 5)