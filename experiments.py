#!/usr/bin/env python3

import numpy as np
import scipy as sp
import termplotlib as tpl
import UliEngineering as ue
import toolz as tlz
import sndalgo as S


def print_sig(dat, title='data', width=130, height=30, base=0):
    fig = tpl.figure()
    datlen = len(dat)
    datx = np.arange(0 + base, base + datlen - 1)

    fig.plot(datx, dat, title=title, width=width, height=height)
    fig.show()

    return dat


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


bsize = 8192
block = np.arange(bsize)

wt = S.waves.square_analog(1, block, 16, bsize)  # square wavetable

print_sig(wt)  # show the wavetable

f = 2  # frequency
s = 48000  # sampling rate
t = np.arange(s)

sig = S.waves.lookup_oscil(f, t, wt, s)
sig2 = S.waves.lookup_oscil(f ** 3, t, wt, s)

mod1 = S.waves.sine(1, block, bsize)
mod1 = S.waves.lookup_oscil(2, t, mod1, s)

sig = mix(sig, sig2)
sig = normalize(sig)

print_sig(sig)

sig = ring(sig, mod1)

print_sig(sig)

