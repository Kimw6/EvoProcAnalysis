import os

from FileProcess.GraphClass import Graph

work_dir = '../data/ecoli/Full'
output_dir = 'Cleaned'
file_list = os.listdir(work_dir)
print(file_list)

n_vertices = {}
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
                source = trans_dict_reverse[v]
                for t in graph.get_vertex(v).get_neighbors():
                    f.write("%d %d\n" % (source, trans_dict_reverse[t.id]))

        n_vertices[index1] = graph.num_vertices
        n_edges[index1] = graph.num_edge
        index1 += 1

print(n_vertices)
print(n_edges)

# CR
# {0: 1409, 1: 1409, 2: 1410, 3: 1421, 4: 1421, 5: 1423, 6: 1424, 7: 1425, 8: 1433, 9: 1433}
# {0: 3735, 1: 3735, 2: 3746, 3: 3778, 4: 3778, 5: 3785, 6: 3788, 7: 3789, 8: 3805, 9: 3805}

# Full
# {0: 2956,     1: 2956,   2: 2949,    3: 2938,    4: 2937,    5: 2939,    6: 2938,    7: 2938,    8: 2940,    9: 2940}
# {0: 23908,    1: 23908,  2: 23907,   3: 23865,   4: 23864,   5: 23871,   6: 23873,   7: 23874,   8: 23888,   9: 23888}
