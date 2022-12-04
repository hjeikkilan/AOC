import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\day3\input3.txt', 'r')
lines = file1.readlines()

points = 0
     
def charToPoints(char):
    if char.isupper():
        return ord(char)-64+26
    if char.islower():
        return ord(char)-96

for i in range(0,len(lines),3):
    # common = list(set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2]))
    common = list(set(lines[i]).intersection(lines[i+1],lines[i+2]))
    common.remove("\n")
    points += charToPoints(common[0])

print(points)
end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")