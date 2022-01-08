#!/usr/bin/env python

import argparse
import json
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results")

args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

performance = [b["times"] for b in results]

fig, ax = plt.subplots()

three_em_times = performance[0]
ypoints_0 = np.array(three_em_times)
ax.plot(ypoints_0, color = 'g', label='3em')
ax.legend()

redstone_times = performance[1]
ypoints_1 = np.array(redstone_times)
ax.plot(ypoints_1, color = 'r', label='redstone')
ax.legend()

ax.set_xlabel('iterations')
ax.set_ylabel('time taken per iteration (s)')

plt.show()
