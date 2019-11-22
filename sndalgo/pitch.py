"""
pitch / pitch conversion and other pitch-related utilities

overview
========

this submodule provides utility functions and classes for pitch,
frequency, midi notes, etc.

optimization with numba
-----------------------

any function that can be compiled using jit with numba will be
compiled.
"""

import numpy as np
import numba as nb

TUNING_FREQUENCY = 440.

@nb.njit
def ntof(note: int) -> float:
    """
    returns the frequency for a given note.
    """

    return TUNING_FREQUENCY * 2 ** ((note - 69) / 12)

@nb.njit
def fton(freq: float) -> float:
    """
    returns a note for the given frequency. use int() to cut of the
    detune.
    """

    return 69 + 12 * np.log2(freq / TUNING_FREQUENCY)

