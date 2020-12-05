#!/usr/bin/env python3

data = []

with open('data.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        data.append(int(line.rstrip()))
        line = reader.readline()
                
for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if(i == j == k):
                continue
            if(data[i] + data[j] + data[k] == 2020):
                print(str(data[i]) + " " + str(data[j])) + " " + str(data[k])
