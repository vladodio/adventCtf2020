#!/usr/bin/env python3

data = []
data2 = []

with open('data.txt', 'r') as reader:
    data = reader.readlines()

tempstr = ""
for i in range(len(data)):
	if(data[i] == '' or data[i] == '\n'):
		data2.append(tempstr)
		tempstr = ""
	else:
		tempstr +=  data[i].strip() + " "

data = data2

counter=0
for i in range(len(data)):
	if(("byr" in data[i]) and ("iyr" in data[i]) and ("eyr" in data[i]) and ("hgt" in data[i]) and ("hcl" in data[i]) and ("ecl" in data[i]) and ("pid" in data[i])):
		counter+=1

print(counter)
