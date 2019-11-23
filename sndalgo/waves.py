import numpy as np
import numba as nb

SAMPLING_RATE=48000

@nb.njit
def sine(freq, t, srate=SAMPLING_RATE) -> np.ndarray:
    srate = srate
    return np.sin(np.pi * 2. * freq * t / srate)


