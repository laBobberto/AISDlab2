def orderProcessing(orderResult, olnyNums = True):
    result = []
    if olnyNums:
        for i in orderResult:
            result.append(i[0])
    else:
        for i in orderResult:
            result.append(str(i[0]) + "b" if i[1]=="black" else "r")
    return result