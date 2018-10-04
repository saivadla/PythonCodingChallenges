path = 'C:\\Users\\C5254143\\Documents\\codingChallenges\\inputdata.txt'

with open(path,'r') as f:
        input = [line.strip() for line in f]
        sort_num = int(input[0])
        del input[0]
        longest=sorted(input, reverse=True, key=len)
        for i in range(0,sort_num):
            print (longest[i])
