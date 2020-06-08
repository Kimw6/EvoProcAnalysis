import os

import matplotlib.pyplot as plt
import numpy as np

from FileProcess.GraphClass import Graph

work_dir = '../data/Mmusculus/Full'
file_list = os.listdir(work_dir)
work_dir2 = '../data/Mmusculus/Full/Cleann'
file_list2 = os.listdir(work_dir2)
print(file_list)
print(file_list2)

n_vert_list_total = []
n_vert_list_nemo = []
n_list_profile = []
relative_frequency = []

cnt = 0
for i in range(len(file_list)):
    rel_freq = []
    filename = file_list[i]
    graph = Graph()
    curPath = work_dir + '/' + filename
    if os.path.isfile(curPath):
        with open(curPath) as f:
            first = True
            for line in f:
                if first:
                    first = False
                    continue
                v1, v2, w = line.split('\t', 2)
                id1 = v1.split('|')[0]
                id2 = v2.split('|')[0]
                graph.add_edge(id1, id2)

        verts = dict.fromkeys(graph.vertices.keys())
        gg = {}

        print(curPath)
        curPath = work_dir + '/Cleann/' + file_list2[cnt]
        print(curPath)
        with open(curPath) as f:
            for line in f:
                if not line.startswith('DIP'):
                    if line.startswith('CF') or line.startswith('CN') or line.startswith('C^') \
                            or line.startswith('C~') or line.startswith('CR') or line.startswith('Cr'):
                        rel_freq.append(float(line.split()[1].replace('%', '')))
                    continue
                else:
                    ll = list(line.split())
                    verts[ll[0]] = list(map(int, ll[1:]))
                    gg[ll[0]] = list(map(int, ll[1:]))
        print('length of nemoprofile nodes and original vertices', len(gg), len(verts))
        profile = [0 for x in range(6)]

        for v in gg:
            for j in range(len(gg[v])):
                profile[j] += gg[v][j]

        for j in range(len(profile)):
            profile[j] = profile[j] / 4
        print(profile)
        n_vert_list_total.append(len(verts))
        n_vert_list_nemo.append(len(gg))
        n_list_profile.append(profile)
        cnt += 1
        relative_frequency.append(rel_freq)

print(relative_frequency)
print(n_vert_list_total)
print(n_vert_list_nemo)
# print(n_list_profile)
# label = ['CF', 'CN', 'CR', 'C^', 'Cr', 'C~']
label = ['CF', 'CN', 'CR', 'C^', 'Cr', 'C~']
n_list_profile = np.array(n_list_profile)

n_list_profile_change = []

# print(n_list_profile)
gens = list(range(0, 10))
plt.xlabel("Generation")
plt.ylabel("Number of node")
plt.title("Node number vs Generations")
for i in range(6):
    temp_list = []
    prev = n_list_profile[:, i][0]
    for temp in n_list_profile[:, i]:
        temp_list.append(temp - prev)
    n_list_profile_change.append(temp_list)

for i in range(6):
    plt.plot(gens, n_list_profile_change[i], label=label[i])

plt.legend()
plt.show()

n_list_profile_change_per = []

for i in range(6):
    temp_list = []
    prev = n_list_profile[:, i][0]
    for temp in n_list_profile[:, i]:
        temp_list.append(100 * (temp - prev) / prev)
    n_list_profile_change_per.append(temp_list)

plt.xlabel("Generation")
plt.ylabel("Percentage of node number change")
plt.title("Percentage Change vs Generations")
for i in range(6):
    plt.plot(gens, n_list_profile_change_per[i], label=label[i])

plt.legend()
plt.show()

label = ['CF', 'CN', 'C^', 'C~', 'CR', 'Cr']

relative_frequency = np.array(relative_frequency)
rel_list = []
for i in range(6):
    temp_list = []
    for temp in relative_frequency[:, i]:
        temp_list.append(temp)
    rel_list.append(temp_list)

for i in range(6):
    plt.xlabel("Generation")
    plt.ylabel("Relative frequency")
    plt.title("Relative frequency vs Generations")
    plt.plot(gens, rel_list[i], label=label[i])
    plt.legend()
    plt.show()


plt.xlabel("Generation")
plt.ylabel("Relative frequency")
plt.title("Relative frequency vs Generations")
for i in range(6):
    plt.plot(gens, rel_list[i], label=label[i])
plt.legend()
plt.show()
