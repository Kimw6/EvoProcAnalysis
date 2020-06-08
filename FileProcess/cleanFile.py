import os

import numpy as np

from FileProcess.GraphClass import Graph
from matplotlib import pyplot as plt


work_dir = '../data/Mmusculus/Full'
output_dir = 'Cleaned'
file_list = os.listdir(work_dir)
print(file_list)

n_vertices = {}
n_disv = []
n_edges = {}
index1 = 0
# file contains connection: A - A
for filename in file_list:
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
        trans_dict = {}
        trans_dict_reverse = {}
        idx = 0
        for v in graph.vertices:
            trans_dict[idx] = v
            trans_dict_reverse[v] = idx
            idx += 1

        output_path = work_dir + '/' + output_dir
        try:
            os.mkdir(output_path)
        except OSError as error:
            print('Folder already created: ', error)

        with open(output_path + '/' + filename, 'w') as f:
            for v in graph.get_vertices():
                for t in graph.get_vertex(v).get_neighbors():
                    f.write("%s %s\n" % (v, t.id))

        n_vertices[index1] = graph.num_vertices
        n_disv.append(graph.num_vertices)
        n_edges[index1] = graph.num_edge
        index1 += 1

print(n_vertices)
print(n_edges)
print(n_disv)
gens = list(range(0, 10))



# plt.plot(gens, sce, ecl)
#
# plt.xlabel('Generation')
# # naming the y axis
# plt.ylabel('Number of nodes')
# plt.title('Number of node vs. Generation')
# # plt.ylim(ymin=0)
# # plt.ylim(ymax=250)
# plt.grid(True)
# plt.show()



# CR
# {0: 1409, 1: 1409, 2: 1410, 3: 1421, 4: 1421, 5: 1423, 6: 1424, 7: 1425, 8: 1433, 9: 1433}
# {0: 3735, 1: 3735, 2: 3746, 3: 3778, 4: 3778, 5: 3785, 6: 3788, 7: 3789, 8: 3805, 9: 3805}

# Full
# {0: 2956,     1: 2956,   2: 2949,    3: 2938,    4: 2937,    5: 2939,    6: 2938,    7: 2938,    8: 2940,    9: 2940}
# {0: 23908,    1: 23908,  2: 23907,   3: 23865,   4: 23864,   5: 23871,   6: 23873,   7: 23874,   8: 23888,   9: 23888}

# Scere
# {0: 5051, 1: 5080, 2: 5084, 3: 5097, 4: 5137, 5: 5144, 6: 5158, 7: 5166, 8: 5176, 9: 5176}
# {0: 44192, 1: 44558, 2: 44614, 3: 44846, 4: 45214, 5: 45333, 6: 45443, 7: 45477, 8: 45597, 9: 45601}

# {0: 1069, 1: 1244, 2: 1331, 3: 1553, 4: 1714, 5: 1969, 6: 2034, 7: 2228, 8: 2259, 9: 2342}
# {0: 1907, 1: 2266, 2: 2497, 3: 3012, 4: 3464, 5: 4097, 6: 4247, 7: 4695, 8: 4854, 9: 5048}
