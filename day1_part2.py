import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AdventOfCode2022\AOC\input1.txt', 'r')
Lines = file1.readlines()

max_cal = 0
id = 0
count = 1
total = 0
top3cal = [0,0,0]
top3ids = [0,0,0]

for line in Lines:
    try:
        total += int(line)
    except(ValueError):
        if total > max(top3cal):
            top3cal.append(total)
            top3ids.append(count)
        if len(top3cal)>3:
            index = top3cal.index(min(top3cal))
            del top3cal[index]
            del top3ids[index]
        total = 0
        count += 1


print("Reindeers {}, {} and {} carries the most amount of calories. Total of: {}".format(top3ids[0],top3ids[1],top3ids[2],sum(top3cal)))

end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")