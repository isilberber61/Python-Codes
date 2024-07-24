def findMax(list):
    #If list is empty
    if not list:
        return None
    
    #We consider the first element as the largest 
    max_number = list[0]

    #We check each element by looping over the list
    for number in list:
        if number > max_number:
            max_number = number

    return max_number

the_list = [17,12,64,51,45,69]
largestNumber = findMax(the_list)
print(f"The largest number in the list is: {largestNumber}")



