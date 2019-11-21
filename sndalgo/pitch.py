"""
pitch / pitch conversion and other pitch-related utilities
"""

import numpy as np
import sympy as sym

f = sym.symbols('f')
p = 69 + sym.log_2(f / 440)

print(p)
