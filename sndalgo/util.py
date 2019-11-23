"""
util.py / utility functions
"""

import numba as nb


def flatten(val) -> list:
    flat = []

    if isinstance(val, list):
        for v in val:
            flat.extend(flatten(v))

    else:
        flat.append(val)

    return flat
