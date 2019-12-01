import numpy as np


def normalize(dat):
    max_ = np.max(np.abs(dat))
    return dat / max_


def mix(*sigs):
    out = np.zeros(len(sigs[0]))

    for sig in sigs:
        out += sig

    return out


def ring(dat, mod):
    out = dat * mod
    return out


def rectify(dat):
    return np.abs(dat)


