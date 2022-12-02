import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\day2\input2.txt', 'r')
Lines = file1.readlines()

points = 0

def numerize(input):
    if input == "A" or input == "X":
        return 1
    if input == "B" or input == "Y":
        return 2
    if input == "C" or input == "Z":
        return 3

def split(input):
    return numerize(input[0]),numerize(input[2]) 

def lokik(a,b):
    if a == b:
        return a + 3
    if a-b == -1 or a-b == 2:
        return b + 6
    else:
        return b

for line in Lines:
    a, b = split(line)
    points += lokik(a,b)

print(points)







end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")