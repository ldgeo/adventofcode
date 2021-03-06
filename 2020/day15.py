"""
Van Eck's sequence

times :

python3.9: 8.9s
pypy3    : 0.7s
"""

startseq = [9,19,1,6,0,5,4]
# iterations = 2020
iterations = 30_000_000

# array of last positions
pos = [0] * iterations

for idx, v in enumerate(startseq[:-1], start=1):
    pos[v] = idx

last = startseq[-1]
for i in range(len(startseq), iterations):
    nextval = i - pos[last] if pos[last] else 0
    pos[last] = i
    last = nextval

print(last)
