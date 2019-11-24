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
def lookup_oscil(freq, t, wave, srate=SAMPLING_RATE):
    """
    takes a waveform lookup table and returns an array of amplitudes
    based on the given frequency
    """

    tablen = len(wave)
    incr = freq * tablen / srate

    out = []

    for v in t:
        x = wave[int(v * incr) % tablen]
        out.append(x)

    return out
