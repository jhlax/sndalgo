import numpy as np
from scipy.signal import butter, filtfilt, freqz, lfilter


def butter_lowpass(cutoff, srate, order=5):
    nyq = 0.5 * srate
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype="low", analog=False)

    return b, a


def butter_lowpass_filter(data, cutoff, srate, order=5):
    b, a = butter_lowpass(cutoff, srate, order=order)
    out = lfilter(b, a, data)
    # out = filtfilt(b, a, data)

    return out


def bfilter(sig, cutoff, srate, order=5, btype="low", force_phase=False):
    nyq = 0.5 * srate
    normal_cutoff = cutoff / nyq

    b, a = butter(order, normal_cutoff, btype=btype, analog=False)

    if force_phase:
        out = filtfilt(b, a, sig)

    else:
        out = lfilter(b, a, sig)

    return out
