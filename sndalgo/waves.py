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
