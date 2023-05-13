def sum_even_tuples(tuples_list):
    total = 0
    for tup in tuples_list:
        if tup[1] % 2 == 0: #checks if second is even 
            total += tup[0]
    return total