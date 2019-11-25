"""
waves.py / waveform generation, oscillators, and synthesis utility functions
"""

__author__ = 'John Harrington'
__version__ = '0.0.2'

import numpy as np
import numba as nb

SAMPLING_RATE = 48000
TWO_PI = np.pi * 2.0


@nb.njit
def sine(freq, t, srate=SAMPLING_RATE) -> np.ndarray:
    """
    this generates a sine wave for the given time integer array `t`
    """

    return np.sin(TWO_PI * freq * t / srate)


@nb.njit
def square(freq, t, srate=SAMPLING_RATE):
    """
    generates a square signal by using an additive synthesis technique with
    the additive function
    """

    BINS = 32
    tamp = total_amp(BINS)

    bins = []

    for idx, i in enumerate(range(BINS)):
        i += 1
        if i % 2 != 0:
            bins.append((1. / ((2. * i - 1) ** 2)) * (2 * i - 1))
        else:
            bins.append(0)

    out = []

    for i in t:
        phs = []
        sums = 0.

        for idx, j in enumerate(bins):
            phs.append(j * sine(idx + 1, i, srate))

        for v in phs:
            sums += v

        out.append(sums)

    m = 0.

    for i in out:
        if abs(i) > m:
            m = abs(i)

    rout = []

    for i in out:
        rout.append(i / m)

    return rout

@nb.njit
def lookup_oscil(freq, t, wave, srate=SAMPLING_RATE):
    """
    takes a waveform lookup table and returns an array of amplitudes
    based on the given frequency

    this is a linear truncating table lookup oscillator
    """

    tablen = len(wave)
    incr = freq * tablen / srate

    out = []

    for v in t:
        x = wave[int(v * incr) % tablen]
        out.append(x)

    return out


@nb.njit
def ilookup_oscil(freq, t, wave, srate=SAMPLING_RATE):
    """
    linear interpolating lookup table oscillator.

    @param freq: frequency integer
    @param t: the time step sequence
    @param wave: the waveform (8192-length recommended)
    @param srate: the sampling rate
    """

    tablen = len(wave)
    incr = freq * tablen / srate

    out = []


@nb.njit
def additive(bins, t, srate=SAMPLING_RATE, normalize=True):
    """
    additive is a function that takes an array of amplitudes for harmonics
    and returns an array that contains the waveform.

    @param bins: array of amplitudes; index 0 is the first harmonic (fundamental)
    @param t: the time range to calculate for
    @param srate: the sampling rate for the calculation
    """

    out = []

    for i in t:
        phs = []

        for idx, j in enumerate(bins):
            phs.append(j * sine(idx + 1, i, srate))

        phs = sum(phs)
        out.append(phs)

    if normalize:
        out = out / np.max(out)

    return out


@nb.njit
def total_amp(n: int) -> float:
    out = 0.

    for z in range(n + 1):
        out += 1. / ((2. * z - 1) ** 2)

    return out
