#!/usr/bin/env python3

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def find_overlap(str):
    counter = 0
    data = str.split()

    for letter in letters:
        letterFound=True
        for response in data:
            if(letter not in response):
                letterFound=False
                break
        if(letterFound):
            counter+=1

                
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
        print(find_overlap(line))
        count += find_overlap(line)
    print(count)
    

def debug():
    pass


if __name__ == '__main__':
    main()
