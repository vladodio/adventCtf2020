#!/usr/bin/env python3

data = []
with open('data.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        data.append(line.rstrip())
        line = reader.readline()

rise = [1,1,1,1,2]
run =  [1,3,5,7,1]

def find_trees(data, rise, run):
    board_width = len(data[0])
    board_height = len(data)
    currentIndex = 0

    counter = 0
    i = rise
    while( i < board_height):
        currentIndex = currentIndex + run
        if(currentIndex >= board_width):
            currentIndex -= board_width

        print('{} {}'.format(currentIndex, i))
        if(data[i][currentIndex] == "#"):
            counter+=1
        i+=rise

    return(counter)


final_solution = 1
for i in range(len(rise)):
    print('rise:{} run:{} trees found:{}'.format(rise[i], run[i], find_trees(data, rise[i],run[i])) )
    final_solution *= find_trees(data, rise[i], run[i])
print(final_solution)
