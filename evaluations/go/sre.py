def match_sequences(elem, secs):
    “””Check if any sec in secs is in elem, returning those which are in elem as a list of strings”””
    return [sec for sec in secs if sec in elem]

def get_common_substrings(first, second):
    “””INPUT: both ‘first’ and ‘second’ are list of strings
        OUTPUT: a list with all subsecs found”””
    result = []
    i, j = 0, 0
    while i < len(first):
        subsecs = []
        while j < len(second):
            if first[i] == second[j]:
                subsecs.append(second[j])
                i++
                j++
            else:
               i++
               j = 0
        result += subsecs
    return result

INPUT: first = “Hello World”
            second = “Thanks for the fish”
OUTPUT: []
            

def exercise(A):
    if len(A) < 2:
        return False, None
    first = A.pop(0).split()
    second = A.pop(0).split()
    secs = get_common_substrings(first, second)
    if not secs:
        return False, None 
    for elem in A:
        secs = match_sequences(elem, secs)
        if not secs:
            return False, None
    
    return True, get_longest(secs)

