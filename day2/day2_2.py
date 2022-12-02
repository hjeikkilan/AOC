import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\day2\input2.txt', 'r')
Lines = file1.readlines()

points = 0

def numerize(input):
    if input == "A" or input == "X": #rock
        return 1
    if input == "B" or input == "Y": # paper
        return 2
    if input == "C" or input == "Z": # scirssors
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

def outcome(match,input):
    if input == 2:
        return match
    if input == 3:
        output = (4+match)%3
    else:
        output = (3+match)%4
    if output == 0:
        return 3
    else:
        return output

for line in Lines:
    a, b = split(line)
    points += lokik(a,outcome(a,b))

print(points)



end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")