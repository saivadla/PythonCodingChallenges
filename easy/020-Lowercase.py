path = 'C:\\Users\\Documents\\codingChallenges\\inputdata.txt'
result = []
with open(path, 'r') as f:
    for fs in f:
        input_split = fs.rstrip('\n').split(" ")
        for num in range(0,len(input_split)):
            if(input_split[num].isupper()):
                result.append(input_split[num].lower())
            else:
                result.append(input_split[num])
print (" ".join(result))
