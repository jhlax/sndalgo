#!/usr/bin/env python3

import numpy as np
import scipy as sp
import termplotlib as tpl
import UliEngineering as ue
import toolz as tlz
import sndalgo as S
from sndalgo.util import *
from sndalgo.dsp import *
from sndalgo.waves import *
from sndalgo.pitch import *
from sndalgo.xenakis import *
from sndalgo.filters import bfilter


bsize = 8192
block = np.arange(bsize)

# wt = S.waves.square_analog(1, block, 16, bsize)  # square wavetable

# print_sig(wt)  # show the wavetable

f = 2  # frequency
s = 48000  # sampling rate
t = np.arange(s)

wform = waveform("square")
oscil = lookup(wform)
out = oscil(1, t)

mod = waveform("harms", 1.0, 0, 0.99)
mod = lookup(mod)
mod = mod(3, t)
mod = fgain(mod, 0.666)
# mod = rectify(mod)

out = ring(out, mod)
out = normalize(out)

out = lookup(out)
out = out(2, t)

highaf = bfilter(out, 4, s, btype="high", order=1, force_phase=True)
lowaf = bfilter(out, 4, s, btype="low", order=1, force_phase=True)

# print(*out, sep=' ')

print_sig(out, title="original")

print_sig(highaf, title="highpass")
print_sig(lowaf, title="lowpass")

# sig = S.waves.lookup_oscil(f, t, wt, s)
# sig2 = S.waves.lookup_oscil(f ** 3, t, wt, s)

# mod1 = S.waves.sine(1, block, bsize)
# mod1 = S.waves.lookup_oscil(2, t, mod1, s)
# mod1 = rectify(mod1)

# sig = mix(sig, sig2)
# sig = normalize(sig)

# print_sig(sig)

# sig = ring(sig, mod1)

# print_sig(sig)
