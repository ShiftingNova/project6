def sum_two(D1, D2):
    '''
    Sum_two takes in two dictionaries. It adds the value of all of the same keys together and puts them
    into a new dictionary called results. Then it returns this new dictionary
    D1 is the parameter for dictionary 1
    D2 is the parameter for the second dictionary
    '''
    results = {}
    for key in D1:
        value = D1[key]
        if key in D2:
            value = value + D2[key]
        results[key] = value
    for key in D2:
        if key not in D1:
            value = D2[key]
            results[key] = value
    return results
def sum_all(list_dictionaries):
    '''
    Sum_all takes in a list of dictionaries and adds together all of the values of the same key in different dictionaries.
    list _dictionaries is the parameter that is a list of dictionaries
    sum_all return the dictionary results
    '''
    results = {}
    for index in list_dictionaries:
        for key in index:
            value = index[key]
            if key not in results:
                results[key] = value
            elif key in results:
                results[key] = results[key] + value
    return results
def two_grams(words):
    '''
    two_grams is a function that takes in a list parameter called words.
    the function then creates tuples for the keys of the dictionary the function returns called results
    the tuples are decided by the words in the list that are next to each other and how often these words are
    next to each other
    '''
    results = {}
    for index in range(len(words)-1):
        temp = (words[index].lower(),words[index+1].lower())
        if temp not in results:
            results[temp] = 1
        else:
            results[temp] = results[temp] + 1
    return results
def keep_first(dictionaries):
    '''
    keep_first takes in a list of dictionaries as the parameter called dictionaries. It returns a singular dictionary
    called results
    It takes the "First Name" and "Last Name" keys
    to create the tuples used for keys of results. The value of the keys isdetermined by the value of the key "GPA" in
    the dictionaries
    '''
    results = {}
    for dict in dictionaries:
        if "GPA" in dict:
            temp = (dict["First Name"], dict["Last Name"])
            if temp not in results:
                results[temp] = dict["GPA"]
    return results
def merge_ascending(L1, L2):
    '''
    merge_ascending takes in two list parameters called L1 and L2.
    then returns a list called results
    results is made by adding the values in L1 and L2 in ascending order
    '''
    results = []
    check = 0
    for index in range(len(L1)):
        results.append(L1[index])
        if index < len(L1)-1:
            if L2[check] < L1[index+1]:
                results.append(L2[index])
                check = check + 1
    while check < len(L2)-1:
        results.append(L2[check])
        check = check + 1
    return results
def start_longest_run(numbers):
    '''
    start_longest_run takes in one list of parameters called numbers. Then counts how many times each number appears in
    the list in a row. then returns the index of the first number in the longest sequence.

    '''
    longest_run = 0
    run = 0
    longest_index = 0
    value = 0
    current_first = 0
    if len(numbers) == 0:
        return (-1)
    for index in range(len(numbers)):
        if numbers[index] != value:
            if run > longest_run:
                longest_run = run
                longest_index = current_first
            current_first = index
            value = numbers[index]
            run = 0
        else:
            run = run+1
    if run > longest_run:
        longest_index = current_first
    return longest_index
def mode(numbers):
    '''
    mode is a function that takes in a list parameter called numbers and counts how often each number appears in the list.
    Then returns the number that appears most in the list.
    This happens by counting each number in the list and
    storing how many ties each number appears in a dictionary.
    if two different numbers appear the same number of times it returns the smaller number
    '''
    results = {}
    if len(numbers)==0:
        return None
    for index in numbers:
        if index not in results:
            results[index] = 1
        else:
            results[index] = results[index]+1
    value = 0
    results_key = 0
    for key in results:
        if results[key] > value:
            results_key = key
            value = results[key]
        elif results[key] == value:
            if results_key > key:
                results_key = key
    return results_key
