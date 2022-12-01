import time

start = time.perf_counter()
# Using readlines()
file1 = open(r'C:\git\AOC\input.txt', 'r')
Lines = file1.readlines()

max_cal = 0
id = 0
count = 1
total = 0 

for line in Lines:
    try:
        total += int(line)
    except(ValueError):
        if total > max_cal:
            max_cal = total
            id = count
        total = 0
        count += 1


print("Reindeer {} carries the most amount of calories. Total of: {}".format(id,max_cal))

end = time.perf_counter()

print(f"Completed in {end - start:0.4f} seconds")