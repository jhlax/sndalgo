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
KEYS = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

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

def nokc(note: float) -> tuple:
    """
    returns a tuple containing (octave, key, cents)
    """

    octave = int((note // 12) - 1)
    key = int(note) % 12
    cents = (note - int(note)) * 100

    return (octave, key, cents)

def note_str(note: float) -> str:
    """
    returns the human-readable string for a note
    """

    o, k, c = nokc(note)
    return f"{KEYS[k]}{o:d}" + (f" {c:+.3f}" if c else "")
