#!/usr/bin/env python3

data = []

with open('data.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        data.append(line.rstrip())
        line = reader.readline()

counter = 0
for i in range(len(data)):
        index1 = int(data[i].split("-")[0]) - 1
        index2 = int(data[i].split("-")[1].split(":")[0].split(" ")[0]) - 1
        letter = data[i].split(" ")[1][0]
        password = data[i].split(" ")[-1]
#        print('{}\n{} {} {} {}'.format(data[i], index1, index2, letter, password))
        atIndex1 = password[index1] == letter
        atIndex2 = password[index2] == letter
        if((atIndex2 and not atIndex1) or (atIndex1 and not atIndex2) ):
                counter+=1
print(counter)
