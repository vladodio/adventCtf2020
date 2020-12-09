#!/usr/bin/env python3
import pickle 

class bag():

	def __init__(self, name, number=1, bags=[]):
		self.name = name
		self.number = number
		self.bags = bags
	
	def __str__(self):
		return self.toString()

	def toString(self, depth=1):
		bagStr = ""
		depth_offset = "    "*depth
		leading_depth_offset = "   "* (depth-1)

		for bag in self.bags:
			bagStr +=  depth_offset +"{}".format(bag.toString(depth+1))
		
		if(bagStr != ""):
			return leading_depth_offset +  'Name: {}   Num: {}\n{}'.format(self.name, self.number, bagStr+'\n')
		else:
			return leading_depth_offset +  'Name: {}   Num: {}\n'.format(self.name, self.number)


	def get_name(self):
		return self.name 

	def return_number(self):
		count = 1
		for bag in self.bags:
			count += bag.return_number()
		return int(count * int(self.number))

	def get_bags(self):
		return self.bags

	def canContain(self, bagName):
		if(self.bags == []):
			return False
		for bag in self.bags:
			if(bagName in bag.get_name()):
				return True
			else:
				if(bag.canContain(bagName)):
					return True
		return False

def processData(data):
	allBags = []
	for i in range(len(data)):
		print(data[i])
		allBags.append(processBag(data[i],1,data))
	return allBags

def processBag(str,num, data):
	str = str.strip()
	bagName = str.split("contain")[0][:-1]
# if there are no bags in the bag
	if("contain no other bags." == str[-22:]):
		return bag(bagName, num)
		
# get the bags in the current bag
	bagsIn = str.split("contain")[1][:-1].split(",")

	for i in range(len(bagsIn)):
		bagsIn[i] = bagsIn[i][1:]
		inBagName = bagsIn[i][bagsIn[i].find(" ")+1:]
		found = False
		for j in range(len(data)):
#			print(data[j][:len(inBagName)])
#			print(inBagName)
			if data[j][:len(inBagName)] == inBagName:
				bagsIn[i] = processBag(data[j], bagsIn[i].split(" ")[0], data)
				found = True
		if(not found):
			bagsIn[i] = bag(inBagName)
			
# add the bag to the list of all bags
	return bag(bagName, num, bagsIn)

def parce_data_into_file():	
	data = []
	with open('data.txt', 'r') as reader:
		data = reader.readlines()
	allBags = processData(data)
	save(allBags)

def save(obj, file='parcedData.bin'):
	with open(file, 'wb') as file:
		pickle.dump(obj, file)

def load(file='parcedData.bin'):
	with open(file, 'rb') as file:
		obj = pickle.load(file)
	return obj


def part1():
	allBags = load()
	counter= 0
	for bag in allBags:
		if(bag.canContain("shiny gold bag")):
			counter+=1
	print(counter)

def part2():
#	allBags = load()
#	index = 89
#	gold_bag = allBags[index]
#	save(gold_bag, "gold_bag.bin")	
	gold_bag = load("gold_bag.bin")
#
#	print(gold_bag.get_name())
	print(str(gold_bag))
	print(gold_bag.return_number())

def main():
	parce_data_into_file()

def debug():
	gold_bag = load("gold_bag.bin")
	print(str(gold_bag.bags[0]))
	print(gold_bag.bags[0].return_number())

def debug2():
	data = []
	with open("data.txt.provided.example", 'r') as reader:
		data = reader.readlines()
	gold_bag = processBag(data[0],1,data)
	print(str(gold_bag))
	print(gold_bag.return_number()-1)



if __name__ == '__main__':
	part2()
