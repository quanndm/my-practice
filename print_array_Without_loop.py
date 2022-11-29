def printNos(n):
    if n == 0:
        return ""
    return str(n) + ' ' + printNos(n - 1)

n = 2
print(printNos(n))