import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from constants import heights




bstWorst = lambda x: x
bstAv = lambda x: 4.311 * math.log2(x)
bstBest = lambda x: math.log2(x)

avlWorst = lambda x: 1.44 * math.log2(x + 2)
avlAv = lambda x: 1.44 * math.log2(x)
avlBest = lambda x: math.log2(x)

rbtWorst = lambda x: 2 * math.log2(x + 1)
rbtAv = lambda x: 2 * math.log2(x)
rbtBest = lambda x: math.log2(x)

def theoryFilling():
    dataTheory = []
    dataTheoryFunc = [[bstWorst, bstAv, bstBest],
                      [avlWorst, avlAv, avlBest],
                      [rbtWorst, rbtAv, rbtBest]]
    for data in dataTheoryFunc:
        currentData = []
        for func in data:
            currentData.append([[x, func(x)] for x in heights])
        dataTheory.append(currentData)
    return dataTheory

def multiPlotCreate(allData, regression, labels, title, printPolynoms, filenameAdd=""):
    colors = ['blue', 'green', 'red', 'gray', 'olive', 'cyan']
    i = 0

    if regression:
        for data in allData:
            points = data
            points = np.array(points)
            x = points[:, 0]
            y = points[:, 1]

            slope_linear, intercept_linear, r_value_linear, _, _ = stats.linregress(x, y)
            y_pred_linear = intercept_linear + slope_linear * x
            r_squared_linear = r_value_linear ** 2

            x_log2 = np.log2(x)
            slope_log, intercept_log, r_value_log, _, _ = stats.linregress(x_log2, y)
            y_pred_log = intercept_log + slope_log * np.log2(x)
            r_squared_log = r_value_log ** 2

            if r_squared_linear > r_squared_log:
                best_model = "Линейная регрессия"
                best_model_eq = f"y = {intercept_linear:.3f} + {slope_linear:.3f}x"
                best_y_pred = y_pred_linear
            else:
                best_model = "Логарифмическая регрессия"
                best_model_eq = f"y = {intercept_log:.3f} + {slope_log:.3f}*log2(x)"
                best_y_pred = y_pred_log

            if best_model == "Линейная регрессия":
                plt.plot(x, best_y_pred, color=colors[i], label=labels[i], zorder=10)
            else:
                x_dense = np.linspace(min(x), max(x), 1000)
                y_dense = intercept_log + slope_log * np.log2(x_dense)
                plt.plot(x_dense, y_dense, color=colors[i], label=labels[i], zorder=10)
            print(title + labels[i] + best_model_eq, sep=" ") if printPolynoms else None
            i+=1


    else:
        for data in allData:

            points = data
            points = np.array(points)
            x = points[:, 0]
            y = points[:, 1]
            plt.scatter(x, y, color=colors[i], label=labels[i], zorder=5)
            i+=1


    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig("Графики/" + filenameAdd + " " + title.replace(".", "_") + ".png")
    plt.close()