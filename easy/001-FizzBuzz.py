path = 'C:\\Users\\Documents\\codingChallenges\\inputdata.txt'
output=[]
with open(path, 'r') as f:
    for fs in f:
        line = fs.rstrip('\n').split(" ")
        lines = map(int,list(line))
        for num in range(1,lines[2]+1):
            if (num % lines[0] == 0):
                output.append("F")
            elif (num % lines[1] == 0):
                output.append("B")
            elif (num % lines[0] == 0 and num % lines[1] == 0):
                output.append("FB")
            else:
                output.append(num)
print  (" ".join(map(str,output)))
