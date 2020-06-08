from matplotlib import pyplot as plt


gens = list(range(0, 10))
sce = [5051, 5080, 5084, 5097, 5137, 5144, 5158, 5166, 5176, 5176]
ecl = [2997, 2945, 2968, 2972, 2986, 2956, 2949, 2937, 2938, 2940]
mmc = [1069, 1244, 1331, 1553, 1714, 1969, 2034, 2228, 2259, 2342]




plt.xlabel('Generation')
# naming the y axis
plt.ylabel('Number of nodes')
plt.title('Number of node vs. Generation')
plt.plot(gens, sce, label='Saccharomyces cerevisiae')
plt.plot(gens, ecl, label='Escherichia coli')
plt.plot(gens, mmc, label='Mus musculus')
plt.legend()
plt.grid(True)
plt.show()


plt.xlabel('File')
# naming the y axis
plt.ylabel('Time (second)')
ss = ['1kb size 3', '1kb size 4', '26kb size 3', '26kb size 4', '200kb size 3', '200kb size 4']
x1 = [0.094, 0.972, 1.992, 70.904, 25.214, 1740]
x2 = [0.217, 0.907, 0.142, 2.467, 11.771, 512.360]
plt.plot(ss, x1, label='Fanmod')
plt.plot(ss, x2, label='Nemo Web Program')
plt.legend()
plt.grid(True)
plt.show()


ece = [3735, 3735, 3746, 3778, 3778, 3785, 3788, 3789, 3805, 3805]
see = [44192, 44558, 44614, 44846, 45214, 45333, 45443, 45477, 45597, 45601]
ms = [1907, 2266, 2497, 3012, 3464, 4097, 4247, 4695, 4854, 5048]
plt.xlabel('Generation')
# naming the y axis
plt.ylabel('Number of edge')
plt.title('Number of edge vs. Generation')
plt.plot(gens, see, label='Saccharomyces cerevisiae')
plt.plot(gens, ece, label='Escherichia coli')
plt.plot(gens, ms, label='Mus musculus')
plt.legend()
plt.grid(True)
plt.show()
