"""
sndalgo / a library for all sorts of code pertaining to sound design and signals

overview
========

this is the sndalgo module.

submodules
----------

* xenakis
* pitch
* util

"""

__version__ = "0.0.2"
__author__ = "John Harrington"

import sndalgo.xenakis
import sndalgo.pitch
import sndalgo.util
import sndalgo.waves
import sndalgo.dsp
import sndalgo.filters

# shortcuts
# from xenakis
from sndalgo.xenakis import Sieve

# from pitch
from sndalgo.pitch import ntof, fton, note_str, KEYS, TUNING_FREQUENCY

# from waves
from sndalgo.waves import waveform, lookup, fourier

# from dsp
from sndalgo.dsp import *

# from filters
from sndalgo.filters import *
