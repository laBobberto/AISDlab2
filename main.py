import sys

from constants import trees_func, heights, cases, trees
from graph import theoryFilling, multiPlotCreate
from processing import generateResult, writeArrays, readArrays, fixData

sys.setrecursionlimit(10000000)


# data = generateResult(trees_func, heights)
dataPractical = readArrays("data.json")
print(len(dataPractical))
dataTheory = theoryFilling()

dataPractical[2] = fixData()

for i in range(3):
    multiPlotCreate(dataTheory[i],True, cases, trees[i], False)
    multiPlotCreate(dataPractical[i],True, cases, trees[i] + ". Регрессия экспериментальных данных", True, " Экспериментальные")
    multiPlotCreate(dataPractical[i],False, cases, trees[i] + ". Экспериментальные данные", True, " Точки")
