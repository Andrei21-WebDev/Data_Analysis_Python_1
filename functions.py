import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.stats import entropy, shapiro, kstest
from seaborn import heatmap

def shannon(x):
    return entropy(x, base=2)

def simpson(x):
    y = x.values
    return 1 - np.sum(x ** 2)

def invsimpson(x):
    y = x.values
    return 1 / np.sum(y ** 2)

def standardizareDate(x, scal=True, nlib=0):
    rez = x - np.mean(x, axis=0)
    if scal:
        rez = rez/np.std(x, axis=0, ddof=nlib)
    return rez

def salvareDate(x, nume_linii, nume_coloane, nume_fisier="out.csv"):
    pd.DataFrame(data=x, index=nume_linii, columns=nume_coloane).to_csv(nume_fisier)