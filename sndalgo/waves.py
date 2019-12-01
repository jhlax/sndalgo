import numpy as np
import numba as nb
from scipy import signal

SAMPLING_RATE = 48000
TWO_PI = np.pi * 2.0


@nb.njit
def sine(freq, t, srate=SAMPLING_RATE) -> np.ndarray:
    """
    this generates a sine wave for the given time integer array `t`
    """

    return np.sin(TWO_PI * freq * t / srate)


@nb.njit
def square_digital(freq, t, srate=SAMPLING_RATE) -> np.ndarray:
    """
    generates a digitally (ideal) square wave using a sine wave and
    signedness
    """

    return np.sign(sine(freq, t, srate))


@nb.njit
def square_harms(nharms) -> np.ndarray:
    out = np.zeros(nharms * 2)

    for idx, harm in enumerate(range(1, 2 * nharms, 2)):
        out[idx * 2] = 4 / (harm * np.pi)

    mx = np.max(np.abs(out))
    out = out / mx

    return out


@nb.njit
def square_analog(freq, t, nharms, srate=SAMPLING_RATE) -> np.ndarray:
    """
    outputs an analog calculation of a square wave dependent on the number
    of harmonics desired

    this outputs a 1:2 Hz square wave, which is the only real way to replicate
    an analog square as it seems
    """

    t_ = t
    t = np.linspace(-1.0, 1.0, srate)

    out = np.zeros(srate)

    for harm in range(1, 2 * nharms, 2):
        # out += (4 / (harm * np.pi)) * np.sin(2 * np.pi * harm * freq * t)
        # out += (4 / (harm * np.pi)) * np.sin(2 * np.pi * harm * freq * t)
        out += -(4 / (harm * np.pi)) * np.sin(np.pi * harm * freq * t)

    mx = np.max(np.abs(out))
    out /= mx

    return out


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
        out = out / np.max(np.abs(out))

    return out


def waveform(name, *harms, bins=64, bsize=8192, norm=True, algo="analog", period=1.0):
    block = np.arange(bsize)
    name = name.strip().lower()

    if name == "sine" and algo == "analog":
        out = sine(period, block, bsize)
        return out

    algo = algo.strip().lower()

    if name == "square" and algo == "analog":
        out = square_analog(period, block, bins, bsize)  # TODO: add normalization
        return out

    if name == "square" and algo == "digital":
        out = square_digital(period, block, bsize)
        return out

    if name == "harms":
        out = additive(harms, block, bsize, norm)
        return out

    return Exception("not a valid input type")


def lookup(wform, srate=48000, trunc=True):
    if trunc:

        def lookup_(freq, t):
            return lookup_oscil(freq, t, wform, srate)

        return lookup_
