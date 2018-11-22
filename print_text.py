import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import math
from random import randint, seed
import os, os.path


fname = "VarelaRound-Regular.ttf"
fpath = os.path.join("./fonts", fname)
prop = fm.FontProperties(fname=fpath)
# rcParams['font.sans-serif'] = ["Varela Round"]

seed()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
with open("./freq_words.txt", "r") as f:
    words = list(map(lambda s: s.strip().upper(), f.readlines()))

rows = math.ceil(math.sqrt(len(words)))
for i in range(rows):
    for j in range(len(words) // rows):
        index = i * rows + j
        if index < len(words):
            w = words[index]
            fontsize = randint(12, 20)
            x = 1 / rows * i
            y = 1 / (len(words) // rows) * j
            prop.set_size(fontsize)
            ax.text(x=x, y=y, s=w,
                    size=fontsize,
                    transform=ax.transAxes,
                    fontproperties=prop)

ax.set_axis_off()
fig.savefig("test.svg")
