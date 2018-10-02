path = 'C:\\Users\\Documents\\codingChallenges\\inputdata.txt'
with open(path, 'r') as f:
    for data in f:
        input_split = data.rstrip('\n').replace(" ","")
        print (input_split)
        double_list = [(int(input_split[num])*2) for num in range(0,len(input_split)) if (input_split[num].isdigit() and (num+1) % 3 == 0)]
        nondouble_list = [int(input_split[num]) for num in range(0,len(input_split)) if (input_split[num].isdigit() and (num+1) % 3 != 0)]
        if (sum(double_list)+sum(nondouble_list) % 10 == 0):
            print ("real")
        else:
            print ("Fake")
