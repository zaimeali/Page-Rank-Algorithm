import numpy as np

def firstIter(gg):
    countNode = len(gg)
    firstCol = np.ones(countNode)/countNode
    return firstCol

# def secondIter(gg, gList):
#     # if 'A' in gg.keys():
#     #     print(True)
#     cList = []
#     dList = []
#     pgRank = []
#     sum = 0
#     outLink = []
#     col = []
#     for key, value in enumerate(gg):
#         # item = value
#         item = value
#         # print(item)
#         for keys, values in enumerate(gg):
#             if not(item == values):
#                 if item in gg[values]:
#                     outLink.append(gg[values])
#                 #     dList.append(values)
#                 #     count = len(gg[values])
#                 #     cList.append(count)
#                 #     countList = len(cList)
#         # print(countList)
#         # print(dList)
#         # print(value)
#         # print(outLink)
#         nrow = len(outLink)
#         for i in range(0, nrow):
#             ncol = len(outLink[i])
#             col.append(ncol)
#         # print(col)
#         # for i in range(0, len(col)):
#         #     for j in range(0, len(col)):
#         #         sum = sum + 0.25 / col[i]
#         #     print(sum)
#         #     sum = 0
#         firstList = len(gList)
#         div = 0
#         for i in range(0, len(col)):
#             if div < firstList:
#                 sum = sum + (gList[div] / col[i])
#                 div = div + 1
#         # print(div)
#         # print(sum)
#         pgRank.append(sum)
#         sum = 0
#         cList = []
#         dList = []
#         outLink = []
#         col = []
#         # print()
#         # if 'A' in value:
#         #     print('True')
#     return pgRank

def Iter(gg, gList):
    outLink = []
    col = []
    pgRank = []
    sum = 0

    for key, value in enumerate(gg):
        item = value
        for keys, values in enumerate(gg):
            if not(item == values):
                if item in gg[values]:
                    outLink.append(gg[values])

        nrow = len(outLink)
        for i in range(0, nrow):
            ncol = len(outLink[i])
            col.append(ncol)

        for i, j in enumerate(gg):
            if item in gg[j]:
                sum = sum + (gList[i]/len(gg[j]))

        pgRank.append(sum)
        sum = 0
        outLink = []
        col = []
    return pgRank


def PageRank(gList, gg):
    maxNum = min(gList)
    maxDict = ''
    sortList = []
    for key, value in enumerate(gg):
        sortList.append(value)
        gList[key] = round(gList[key], 3)

    n = len(gList)

    for i in range(len(gList)):

        for j in range(0, n-i-1):
            if gList[j] > gList[j+1]:
                gList[j], gList[j+1] = gList[j+1], gList[j]
                sortList[j], sortList[j+1] = sortList[j+1], sortList[j]


    print(sortList)
    return (gList, sortList)




# Graph Initialize
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}
print(graph)
print()
print('Total Nodes are: ', len(graph))
print()
print('First Iteration')
first = firstIter(graph)
print(first)
print()
print('Second Iteration')
second = Iter(graph, first)
print(second)
print()
print('Third Iteration')
third = Iter(graph, second)
print(third)
print()
print()
print(" ", "1st Iteration ", "2nd Iteration ", "3rd Iteration ")
for key, value in enumerate(graph):
    print(value, "     ", first[key], "       ", round(second[key], 4), "       ", round(third[key], 4))

indx, keyName = PageRank(third, graph)
print()
print("4 = Highest ~ 1 = Lowest")
for i in range(0, len(indx)):
    print(indx[i], ":", keyName[i])
