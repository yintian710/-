# coding:utf-8

import math


def f(x, y):
    return 1 / (1 + x * x) - 2 * y * y
    # return -y + x + 1


def Euler(x, y, h, n):
    E = [y]
    for i in range(0, n):
        y = y + h * f(x, y)
        E.append(y)
        x += h
    return E


def trapezoid(x, y, h, n):
    T = [y]
    for i in range(0, n):
        # k1 = h * f(x, y)
        # k2 = h * f(x+h, k1)
        # y = y + (k1 + k2) / 2
        y1 = y + h*f(x, y)
        y = y + h/2 * (f(x, y) + f(x+h, y1))
        x += h
        T.append(y)
    return T


def solution(x, h, n):
    S = []
    for i in range(0, n):
        # y = x + math.e ** (-x)
        y = x/(1 + x*x)
        S.append(y)
        x += h
    return S


if __name__ == '__main__':
    x0 = 0
    y0 = 0
    h = 0.1
    n = 11
    E = Euler(x0, y0, h, n)
    T = trapezoid(x0, y0, h, n)
    S = solution(x0, h, n)
    for i in range(1, n):
        print(i, "%.6f" % E[i], "%.6f" % T[i], "%.6f" % S[i],"%.6f" %(E[i]-S[i]),"%.6f" %(T[i]-S[i]))
