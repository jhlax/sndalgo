"""
util.py / utility functions
"""

import numpy as np
import numba as nb
import termplotlib as tpl


def flatten(val) -> list:
    flat = []

    if isinstance(val, list):
        for v in val:
            flat.extend(flatten(v))

    else:
        flat.append(val)

    return flat


@nb.njit
def softmax(tab):
    z = np.exp(np.abs(tab))
    m = np.max(np.abs(z))
    out = z / m

    return out


def print_sig(dat, title="data", width=130, height=30, base=0):
    fig = tpl.figure()
    datlen = len(dat)
    datx = np.arange(0 + base, base + datlen - 1)

    fig.plot(datx, dat, title=title, width=width, height=height)
    fig.show()

    return dat
