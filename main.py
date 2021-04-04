baseGraphPoints = {
    1: {2: 20, 8: 29, 12: 29, 13: 37},
    2: {1: 20, 3: 25, 8: 28, 12: 39},
    3: {2: 25, 4: 25, 8: 30, 13: 54},
    4: {3: 25, 5: 39, 6: 32, 7: 42, 9: 23, 10: 33, 14: 56},
    5: {4: 39, 6: 12, 7: 26, 10: 19},
    6: {4: 32, 5: 12, 7: 17, 10: 35, 11: 30},
    7: {4: 42, 5: 26, 6: 17, 11: 38},
    8: {1: 29, 2: 28, 3: 30, 12: 25, 13: 22},
    9: {4: 23, 10: 26, 13: 34, 14: 37, 16: 43},
    10: {4: 33, 5: 19, 6: 35, 9: 26, 11: 24, 14: 30, 15: 19},
    11: {6: 30, 7: 38, 10: 24, 15: 26, 18: 36, },
    12: {1: 29, 2: 39, 8: 25, 13: 27, 16: 43, },
    13: {1: 37, 3: 54, 8: 22, 9: 34, 12: 27, 14: 24, 16: 19},
    14: {4: 56, 9: 37, 10: 30, 13: 24, 15: 20, 16: 19, 17: 17},
    15: {10: 19, 11: 26, 14: 20, 17: 18, 18: 21},
    16: {9: 43, 12: 43, 13: 19, 14: 19, 17: 26},
    17: {14: 17, 15: 18, 16: 26, 18: 15},
    18: {11: 36, 15: 21, 17: 15},
}


def calculatePathCost(allPaths):
    costAllPaths = {}

    for path in allPaths:
        costAllPaths[calculateSinglePathCost(path)] = path

    return costAllPaths


def calculateSinglePathCost(path):
    totalCost = 0

    for i in range(0, len(path)):
        if path[i] != path[-1]:
            totalCost += baseGraphPoints[path[i]][path[i + 1]]

    return totalCost


def sortPathByCost(costAllPaths):
    for (i, cost) in enumerate(sorted(costAllPaths)):
        if i < 5:
            filteredObject = {}
            filteredObject['Custo'] = cost
            filteredObject['Caminho'] = costAllPaths[cost]
            print(filteredObject)


def checkPathRecursive(current, path, allPaths, endNode):
    for currentGraphPoint in baseGraphPoints[current].keys():
        if currentGraphPoint in path:
            continue
        elif currentGraphPoint == endNode:
            allPaths.append(path + [currentGraphPoint])
        else:
            checkPathRecursive(currentGraphPoint,
                               (path + [currentGraphPoint]), allPaths, endNode)


def calcPaths(startNode, endNode):
    allPaths = []

    checkPathRecursive(startNode, [startNode], allPaths, endNode)
    sortPathByCost(calculatePathCost(allPaths))


calcPaths(3, 13)
