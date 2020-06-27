# Решение с помощью easygui

import math
import easygui
import numpy as np
from easygui import *

msg = "Решение СЛАУ 3х3"
title = "Решение квадратного уравнения"
fieldNames = ["a11, a12, a13", "a21, a22, a23",
              "a31, a32, a33", "b1, b2, b3"]
fieldValues = []
fieldValues = multenterbox(msg, title, fieldNames, [
                           "15, 25, 35", "9, 8, 7", "18, 12, 10", "12, 13, 14"])

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "":
        break  # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

A = [[], [], [], []]
i = -1

for el in fieldValues:
    i += 1
    line = el.split(',')
    line = [A[i].append(float(elem.strip())) for elem in line]

B = A.pop()
A = np.array(A)
B = np.array(B)

X = np.linalg.solve(A, B)
# Выполнил Попов Н
print("X = ", X)

result = "x1 = " + str(round(X[0], 2)) + "; x2 = " + \
    str(round(X[1], 2)) + "; x3 = " + str(round(X[2], 2))

msgbox(str(result), "Результат вычислений")
