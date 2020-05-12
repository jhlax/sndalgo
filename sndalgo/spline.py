from collections import namedtuple
from random import randint

import numpy as np
from matplotlib.pyplot import plot, show
from numba import njit


def create_spline(x, y):
    """
    creates a spline ready for use in interpolation.

    :param x:
    :param y:
    :return:
    """

    x = np.asfarray(x)
    y = np.asfarray(y)

    # remove non finite values
    indexes = np.isfinite(x)
    x = x[indexes]
    y = y[indexes]

    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size - 1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = np.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = np.sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = np.sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    return x, y, z


def interp_spline(x0, x, y, z):
    """
    calculate the value for x0 in a spline

    :param x0:
    :param x:
    :param y:
    :param z:
    :return:
    """

    size = len(x)

    # find index
    index = np.asarray(x.searchsorted(x0), dtype=bool)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0
    # print(xi0, xi1, yi0, yi1, zi0, zi1)

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 + zi1 / (6 * hi1) * (x0 - xi0) ** 3 + (yi1 / hi1 - zi1 * hi1 / 6) * (
            x0 - xi0) + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)

    return f0


class SplineInterpolator:
    def __init__(self, x, y):
        self.x, self.y, self.z = create_spline(x, y)

    def interpolate(self, x0):
        return interp_spline(x0, self.x, self.y, self.z)


class SplineWaveInterpolator(SplineInterpolator):
    def __init__(self, x, y):
        super(SplineWaveInterpolator, self).__init__(x, y)
        self.size = len(x)
        self.phases = np.linspace(0, 1, self.size, dtype=float)

    def interpolate(self, x0):
        x0 = np.fmod(x0, np.ones(len(x0), dtype=float))
        return interp_spline(x0, self.x, self.y, self.z)


class SplineWaveFrame:
    spline: SplineWaveInterpolator = None

    def __init__(self, waveform):
        self.x = waveform
        self.y = np.arange(len(waveform), dtype=float)
        self.update_spline()

    def update_spline(self):
        self.spline = SplineWaveInterpolator(self.x, self.y)

    def get(self, x0):
        x0 = np.asfarray(x0)
        return self.spline.interpolate(x0)

    def get_samp(self, x0):
        x0 = np.asfarray(x0)
        return self.spline.interpolate(x0 / self.spline.size)


spline = SplineWaveFrame(np.sin(2 * np.pi * np.linspace(0, 2, 64)))


# FIXME: get this working please.
# print(spline.get(np.linspace(0, 1, 64, dtype=float)))


def cubic_interp1d(x0, x, y):
    """
    Interpolate a 1-D function using cubic splines.
      x0 : a float or an 1d-array
      x : (N,) array_like
          A 1-D array of real/complex values.
      y : (N,) array_like
          A 1-D array of real values. The length of y along the
          interpolation axis must be equal to the length of x.

    Implement a trick to generate at first step the cholesky matrice L of
    the tridiagonal matrice A (thus L is a bidiagonal matrice that
    can be solved in two distinct loops).

    additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf
    """
    x = np.asfarray(x)
    y = np.asfarray(y)

    # remove non finite values
    # indexes = np.isfinite(x)
    # x = x[indexes]
    # y = y[indexes]

    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size - 1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = np.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = np.sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = np.sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 + zi1 / (6 * hi1) * (x0 - xi0) ** 3 + (yi1 / hi1 - zi1 * hi1 / 6) * (
            x0 - xi0) + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)

    return f0


@njit
def hermite_interp(y0: float, y1: float, y2: float, y3: float, mu: float, tension: float = 0, bias: float = 0) -> float:
    """

    double hermite_interp(double y0, double y1, double y2, double y3, double mu,
                          double tension, double bias) {
        double m0, m1, mu2, mu3;
        double a0, a1, a2, a3;

        mu2 = mu*mu;
        mu3 = mu2*mu;

        m0  = (y1-y0) * (1+bias) * (1-tension)/2;
        m0 += (y2-y1)*(1-bias)*(1-tension)/2;
        m1  = (y2-y1)*(1+bias)*(1-tension)/2;
        m1 += (y3-y2)*(1-bias)*(1-tension)/2;

        a0 =  2*mu3 - 3*mu2 + 1;
        a1 =    mu3 - 2*mu2 + mu;
        a2 =    mu3 -   mu2;
        a3 = -2*mu3 + 3*mu2;

        return(a0*y1+a1*m0+a2*m1+a3*y2);
    }

    """

    mu1, mu2 = mu ** 2, mu ** 3

    m0 = (y1 - y0) * (1 + bias) * (1 - tension) / 2
    m0 += (y2 - y1) * (1 - bias) * (1 - tension) / 2
    m1 = (y2 - y1) * (1 + bias) * (1 - tension) / 2
    m1 += (y3 - y2) * (1 - bias) * (1 - tension) / 2

    a0 = 2 * mu2 - 3 * mu1 + 1
    a1 = mu2 - 2 * mu1 + mu
    a2 = mu2 - mu1
    a3 = -2 * mu2 + 3 * mu2

    hermitian = (a0 * y1 + a1 * m0 + a2 * m1 + a3 * y2)

    return hermitian


def calculate_mus(mu):
    return mu, mu ** 2, mu ** 3


def calculate_tension(tens):
    return 1 - tens


def calculate_biases(bias):
    return 1 + bias, 1 - bias


def calculate_ms(ys: (tuple, list), biases: (tuple, list), tens: (float, int)):
    ms = [0, 0]

    for m_i in range(2):
        if m_i % 2 == 0:
            mul = 1
        else:
            mul = -1

        ms[m_i] = sum([(ys[1 + m_i * 2] - ys[0 + m_i * 2]) * (1 - mul * bias) * (1 - tens) / 2 for bias in biases])

    return ms


SPLINE = namedtuple('SPLINE', 'ys ms')


def spline_for(ys, bias, tension):
    biases = calculate_biases(bias)
    ms = calculate_ms(ys, biases, tension)

    return ms, biases


def calculate_as(mus):
    mu, mu1, mu2 = mus

    a0 = 2 * mu2 - 3 * mu1 + 1
    a1 = mu2 - 2 * mu1 + mu
    a2 = mu2 - mu1
    a3 = -2 * mu2 + 3 * mu2

    return a0, a1, a2, a3


def spline_interp(ys, ms, mu):
    mus = calculate_mus(mu)
    a = calculate_as(mus)

    print(a, ys, ms, mus)

    # return a[0] * ys[0] + a[1] * ms[0] + a[2] * ms[1] + a[3] * ys[2]
    return a[0] * ys[0] + a[1] * ms[0] + a[2] * ms[1] + a[3] * ys[2]


class SplineTable:
    def __init__(self, y, bias=0, tension=0):
        self.y = y
        self.bias = bias
        self.tension = tension
        splines = []
        for i in range(len(y) - 3):
            yr = y[0 + i: 4 + i]
            splines.append((yr, spline_for(yr, tension, bias), list(range(i, i + 4))))
        self.splines = splines

    def get_value_at(self, x: float):
        index = None
        cur = 0
        mu = 0
        while index is None:
            if self.splines[cur][2][0] <= x <= self.splines[cur][2][1]:
                index = cur
                mu = cur + 1 - x
            cur += 1
            if cur == len(self.splines):
                raise ValueError("Spline not in here!")

        spline = self.splines[index][1]

        return spline_interp(self.splines[index][0], spline[0], mu)

    __getitem__ = get_value_at


# FIXME: SO CLOSE YET SOMETHING ESCAPES ME
def cr_spline_coefficients(Y):
    a0 = -0.5 * Y[0] + 1.5 * Y[1] - 1.5 * Y[2] + 0.5 * Y[3]
    a1 = Y[0] - 2.5 * Y[1] + 2 * Y[2] - 0.5 * Y[3]
    a2 = -0.5 * Y[0] + 0.5 * Y[2]
    a3 = Y[1]

    return [a0, a1, a2, a3]

# def cr_spline_


def cr_spline(A, mu):
    """
    the Catmull-Rom spline calculated
    :param Y:
    :param mu:
    :return:
    """
    mu, mu2 = mu, mu ** 2

    return A[0] * mu * mu2 + A[1] * mu2 + A[2] * mu + A[3]
