# Решение с использованием easygui

import math
import easygui
from easygui import *

msg = "Решить квадратное уравнение вида: ax^2 + bx + c = 0"
title = "Решение квадратного уравнения"
fieldNames = ["a", "b", "c"]
fieldValues = []
fieldValues = multenterbox(msg, title, fieldNames)

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

arr = []
# Выполнил Попов Н
for el in fieldValues:
    arr.append(float(el))

a, b, c = arr

D = b**2 - 4 * a * c

if (D < 0):
    result = "D < 0, нет решений"
elif (D == 0):
    x1 = -b / (2 * a)
    result = "Единственное решение x = " + str(x1)
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    result = "Уравнение имеет два корня x1 = " + \
        str(round(x1, 2)) + "; x2 = " + str(x2)

msgbox(str(result), "Результат вычислений")
