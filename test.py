# from sndalgo.xenakis import Sieve

# major_scale = Sieve("-3@2&4|-3@1&4@1|3@2&4@2|-3@0&4@3")
# notes = major_scale.set(range(0, 25))

# ots = Sieve("1@7") & "3@1" & (7, 3, False)

# print("major scale")
# print(major_scale, major_scale.set(range(0, 25)), sep="\n")
# print()
# print("digits of 137")
# print(ots, ots.simple, ots.set(range(0, 25)), sep="\n")
# print()

# import sndalgo.pitch as sa

# print("62:", sa.note_str(62))

# def flatten(val) -> list:
#     flat = []

#     if any(isinstance(val, _) for _ in [list, tuple, set]):
#         for v in val:
#             flat.extend(flatten(v))

#     else:
#         flat.append(val)

#     return flat

# from sndalgo.util import flatten

# testval = [[3, [2]], [[[[5]]]]]

# print(testval, 'flattened:', flatten(testval))

# import numpy as np

# from sndalgo.waves import sine, lookup_oscil
# from sndalgo.pitch import ntof

# waveform = sine(1, np.arange(8192), 8192)
# waveform = lookup_oscil(30, np.arange(48000), waveform, 48000)

# print(*waveform, sep="\n")

import numpy as np
import termplotlib as tpl

from sndalgo.waves import additive, lookup_oscil, square_digital, square_analog
from sndalgo.util import softmax

bsize = 8192

z = np.arange(bsize)
f = 1

h = np.asarray([1.0, 1.0, 1.0], dtype=float)

S = np.arange(48000)
# y = additive(h, z, s, True)
# y = lookup_oscil(3, x, y, 48000)
x = np.arange(bsize)
y = square_analog(1, z, 16, bsize)
y = lookup_oscil(2, S, y, len(S))

fig = tpl.figure()

x = np.arange(len(y))

fig.plot(x, y, label='additive', width=130, height=30)

fig.show()

print(np.max(y))

# print(*y, sep="\n")

# print(total_amp(4))

# for v in lookup_oscil(2, z, wave, 48000):
#     print(v)

# print(additive([1, 0, 1, 0], 8192, 8192))

# wt = additive([0.28, 0.31, 0.7, 0.19, 0.18, 0.1], np.arange(8192), 8192)

# _ = [print(x) for x in lookup_oscil(2, np.arange(44200), wt, 44200)]

print('\a')
