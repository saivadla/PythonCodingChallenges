
path = 'C:\\Users\\C5254143\\Documents\\codingChallenges\\inputdata.txt'

with open(path,'r') as f:
    for line in f:
        input = line.rstrip("\n").split(" ")
        search_num = input[-1]
        print (input[-int(search_num)-1])
