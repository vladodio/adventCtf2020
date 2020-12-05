#!/usr/bin/env python3

data = []
processedInput = []
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def check_hex(str):
        for ch in str:
                if ((ch < '0' or ch > '9') and (ch < 'a' or ch > 'f')):
                        return False
        return True

def check_all_fields_exist(data):
    return(("byr" in data) and ("iyr" in data) and ("eyr" in data) and ("hgt" in data) and ("hcl" in data) and ("ecl" in data) and ("pid" in data))

def check_passport_with_all_fields(data):

# check birth year
    indexOfField = data.index(fields[0])
    if(int(data[indexOfField+1]) < 1920 or int(data[indexOfField+1]) > 2002):
        print(data[indexOfField+1])
        return False
# check issue year
    indexOfField = data.index(fields[1])
    if(int(data[indexOfField+1]) < 2010 or int(data[indexOfField+1]) > 2020):
        print(data[indexOfField+1])
        return False
# check eye color
    indexOfField = data.index(fields[2])
    if(int(data[indexOfField+1]) < 2020 or int(data[indexOfField+1]) > 2030):
        print(data[indexOfField+1])
        return False

# check height
    indexOfField = data.index(fields[3])
    if(data[indexOfField+1][-2:] == "cm"):
        if(int(data[indexOfField+1][:-2]) < 150 or int(data[indexOfField+1][:-2]) > 193):
            print(data[indexOfField+1])
            return False

    elif(data[indexOfField+1][-2:] == "in"):
        if(int(data[indexOfField+1][:-2]) < 59 or int(data[indexOfField+1][:-2]) > 76):
            print(data[indexOfField+1])
            return False

    else:
        return False


# check hair color
    indexOfField = data.index(fields[4])
    if(not (check_hex(data[indexOfField+1][1:]) and data[indexOfField+1][0] == "#")):
        print(data[indexOfField+1])
        return False

# check ecl
    indexOfField = data.index(fields[5])
    if(not (data[indexOfField+1] in eye_colors)):
        print(data[indexOfField+1])
        return False

# check pid
    indexOfField = data.index(fields[6])
    if(not (data[indexOfField+1].isdigit() and len(data[indexOfField+1]) == 9)):
        return False
    return True


def main():
    with open('data.txt', 'r') as reader:
        data = reader.readlines()

    tempstr = ""
    for i in range(len(data)):
            if(data[i] == '' or data[i] == '\n'):
                    processedInput.append(tempstr)
                    tempstr = ""
            else:
                    tempstr +=  data[i].strip() + " "


    counter=0
    counter2 = 0
    indexOfField = 0
    for i in range(len(processedInput)):
        data = processedInput[i].replace(" ", ":").split(":")[:-1]
        if(not check_all_fields_exist(data)):
            continue
        if(check_passport_with_all_fields(data)):
            counter+=1

    print(counter)

if __name__ == '__main__':
    main()
