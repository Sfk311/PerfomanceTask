import sys

a = sys.argv[1]
file = open(a, "r")

l = []
while True:
    line = file.readline()
    if not line:
        break
    l.extend(line.strip().split())
    nums = [int(i) for i in l]

turns = 9**99
sum = 0

for i in nums:
    for j in nums:
        sum += abs(i -j)
    if sum < turns:
        turns = sum
    sum = 0

print(turns)