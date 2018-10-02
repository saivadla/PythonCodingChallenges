import itertools
import operator
path = 'C:\\Users\\Documents\\codingChallenges\\inputdata.txt'
with open(path, 'r') as f:
    for fs in f:
        input_split = fs.rstrip('\n').split(",")
        input_split = map(int,input_split)
        for num in itertools.count(start=1,step=1):
            if (input_split[1] * num >= input_split[0]):
                print (input_split[1]*num)
                break
