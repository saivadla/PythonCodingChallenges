import more_itertools
path = 'C:\\Users\\C5254143\\Documents\\codingChallenges\\inputdata.txt'

with open (path,'r') as f:
    for lines in f:
        input=lines.split(" ")
        print (" ".join(list(more_itertools.unique_everseen([i for i in input if (input.count(i) > 2) ]))))
        
