#!/usr/bin/env python3

def readData(file='data.txt'):
	data = []
	with open(file, 'r') as reader:
	    data = reader.readlines()
	return data

class program():

	def __init__(self, data, starting_index=0, accumulator=0):
		self.data = data
		self.index = starting_index
		self.LAST_INDEX = len(data) -1
		self.accum = accumulator
		self.clean_data()

	def clean_data(self):
		for i in range(len(self.data)):
			self.data[i] = self.data[i].strip()

	def process_instruction(self):
#		print(self.data[self.index])
		instruction = self.data[self.index].split(" ")
		if(instruction[0] == "nop"):
			self.index+=1
		elif(instruction[0] == "acc"):
			self.accum+= int(instruction[1])
			self.index+=1
		elif(instruction[0] == "jmp"):
			self.index += int(instruction[1])
		return self.index

	def get_accum(self):
		return self.accum

	def get_instruction():
		return self.data[self.index].split(" ")[0]

	def check_for_loop(self):
		addresses_visited = set()
		while(True):
			self.index = self.process_instruction()
			if(self.index in addresses_visited):
				return True
			elif(self.index >= self.LAST_INDEX):
				return False
			else:
				addresses_visited.add(self.index)


def part1():
	data = readData()
	test = program(data)
	test.check_for_loop()
	print(test.get_accum())

def part2():
	data = readData()

	jmp_indexes = []
	nop_indexes = []
	for i in range(len(data)):
		if(data[i][:3] == "jmp"):
			jmp_indexes.append(i)
		if(data[i][:3] == "nop"):
			nop_indexes.append(i)

	for index in nop_indexes:
		modified_data = data.copy()
		modified_data[index] = "jmp " + modified_data[index].split(" ")[1]
		test =  program(modified_data)
		if(not test.check_for_loop()):
			print(test.get_accum())

	for index in jmp_indexes:
		modified_data = data.copy()
		modified_data[index] = "nop " + modified_data[index].split(" ")[1]
		test =  program(modified_data)
		if(not test.check_for_loop()):
			print(test.get_accum())
			

def main():
	part2()


def debug():
	pass

if __name__ == '__main__':
	main()
