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

from sndalgo.waves import additive, lookup_oscil

bsize = 8196

z = np.arange(bsize)
f = 1
s = bsize

h = np.asarray([1.0, 0.8, 0.6, 0, 0.5, 0, 0.4], dtype=float)

y = additive(h, z, s, True)

y = lookup_oscil(3, np.arange(48000), y, 48000)

print(*y, sep='\n')
