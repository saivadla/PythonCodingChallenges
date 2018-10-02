path = 'C:\\Users\\Documents\\codingChallenges\\inputdata.txt'
output=[]
with open(path, 'r') as f:
    for fs in f:
        input_split = fs.rstrip('\n').split(" ")
        print (" ".join(input_split[::-1]))
