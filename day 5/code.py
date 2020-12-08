#!/usr/bin/env python3


def process_boarding_pass(str, rowMax=128, colMax=8):
	row = process_fb(str[-3:], rowMax)
	col = process_lr(str[:-3], colMax)
	return([row,col])

def process_fb(str, rowMax=128):
	bounds = [0, rowMax]
	diff = rowMax
	while(str != ""):
		if(str[0] == "F"):
			diff = diff// 2
			bounds[1] = bounds[1]//2
		else:
			diff = diff//2
			bounds[0] += diff 
		str = str[1:]
	return bounds[0]

def process_lr(str, colMax=8):
	bounds = [0, colMax]
	diff = colMax
	while(str != ""):
		if(str[0] == "L"):
			diff = diff// 2
			bounds[1] = bounds[1]//2
		else:
			diff = diff//2
			bounds[0] += diff 
		str = str[1:]
	return bounds[0]

def main():
	data = []
	with open('data.txt', 'r') as reader:
	    line = reader.readline()
	    while line != '':
	        data.append(line.rstrip())
	        line = reader.readline()
	largest = 0

	for line in data:
		num = process_boarding_pass(line)
		if((num[0]*40 + num[1]) > largest):
			largest = num[0]*40 + num[1]
			print(line)
			print(num)
	print(largest)

def debug():
	print(process_fb("FBFBBFFRLR"))


if __name__ == '__main__':
	main()
