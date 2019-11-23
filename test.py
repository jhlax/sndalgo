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

import sndalgo.pitch as sa

print("62:", sa.note_str(62))
