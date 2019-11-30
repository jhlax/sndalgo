"""
util.py / utility functions
"""

import numpy as np
import numba as nb


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
