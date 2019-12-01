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


bsize = 8192
block = np.arange(bsize)

wt = S.waves.square_analog(1, block, 16, bsize)  # square wavetable

# print_sig(wt)  # show the wavetable

f = 2  # frequency
s = 48000  # sampling rate
t = np.arange(s)

wform = waveform("harms", 1.0, 0., 0.222, 0., 0., 0.090909)
oscil = lookup(wform)
out = oscil(2, t)

mod = waveform("sine")
mod = lookup(mod)
mod = mod(4, t)
mod = rectify(mod)

out = ring(out, mod)

print_sig(out)


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
