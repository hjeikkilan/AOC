import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\day3\input3.txt', 'r')
Lines = file1.readlines()

points = 0

def split(input):
    length = len(input)
    return input[0:int(length/2)],input[int(length/2):length]
     

def charToPoints(char):
    if char.isupper():
        return ord(char)-64+26
    if char.islower():
        return ord(char)-96

for line in Lines:
    a,b = split(line)
    common = list(set(a).intersection(b))
    points += charToPoints(common[0])

print(points)
end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")