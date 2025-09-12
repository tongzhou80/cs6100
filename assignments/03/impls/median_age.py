import sys

def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 0:
        return (values[n//2 - 1] + values[n//2]) / 2.0
    else:
        return values[n//2]

ages = []
with open(sys.argv[1], "r") as f:
    next(f)  # skip header
    for line in f:
        parts = line.strip().split(",")
        ages.append(int(parts[2]))

print(median(ages))
