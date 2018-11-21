import matplotlib.pyplot as plt
import math
from random import randint, seed

seed()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
with open("./freq_words.txt", "r") as f:
    words = list(map(lambda s: s.strip(), f.readlines()))

rows = math.ceil(math.sqrt(len(words)))
for i in range(rows):
    for j in range(len(words) // rows):
        index = i * rows + j
        w = words[index]
        fontsize = randint(12, 20)
        x = 1 / rows * i
        y = 1 / rows * j
        ax.text(x=x, y=y, s=w,
                fontsize=fontsize,
                transform=ax.transAxes)

ax.set_axis_off()
fig.savefig("test.svg")
