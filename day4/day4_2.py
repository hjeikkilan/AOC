import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\day4\input4.txt', 'r')
Lines = file1.readlines()

points = 0

def split(input):
    input = input.replace('\n', '')
    input = input.split(',')
    return input[0],input[1]

def fillCaps(input):
    input = input.split('-')
    newList = []
    for i in range(int(input[0]),int(input[1])+1,1):
        newList.append(i)
    return newList

for line in Lines:
    a,b = split(line)
    a,b = fillCaps(a),fillCaps(b)
    common = list(set(a).intersection(b))
    if len(common) > 0:
        points += 1

print(points)

end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")