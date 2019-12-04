import numpy as np
import numba as nb


@nb.njit
def normalize(dat):
    max_ = np.max(np.abs(dat))
    return dat / max_


@nb.njit
def mix(*sigs):
    out = np.zeros(len(sigs[0]))

    for sig in sigs:
        out += sig

    return out

@nb.njit
def fgain(dat, amp):
    out = dat * amp

    return out


@nb.njit
def ring(dat, mod):
    out = dat * mod
    return out


@nb.njit
def rectify(dat):
    return np.abs(dat)
