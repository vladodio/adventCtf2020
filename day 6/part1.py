#!/usr/bin/env python3

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def count_unique(str):
    counter = 0
    for letter in letters:
        if(letter in str):
            counter += 1
    return counter

def main():
    data = []
    data2 = []
    tempstr = ""
    with open('data.txt', 'r') as reader:
        data = reader.readlines()
    for i in range(len(data)):
        if(data[i] == '' or data[i] == '\n'):
            data2.append(tempstr)
            tempstr = ""
        else:
            tempstr +=  data[i].strip() + " "
    data = data2


    count = 0
    print(data)
    for line in data:
        print(count_unique(line))
        count += count_unique(line)
    print(count)
    

def debug():
    pass


if __name__ == '__main__':
    main()
