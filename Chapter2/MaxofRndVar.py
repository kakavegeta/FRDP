# 2.1 Maximum of random variable - statistic extremes

from math import log


def Possibility(vars, lambdap):
    maxvar = max(vars)
    p = lambdap / maxvar
    return -log(p) / len(vars)
