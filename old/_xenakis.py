class XenakisObject(object):
    def __call__(self, *args, **kwargs) -> list:
        raise NotImplementedError()

    def __and__(self, other: 'XenakisObject') -> 'XenakisObject':
        raise NotImplementedError()

    def __or__(self, other: 'XenakisObject') -> 'XenakisObject':
        raise NotImplementedError()


class Sieve(XenakisObject):
    """
    Xenakis Sieve, which is a collection of groups of Residuals created
    with ands and then joined with ors.
    """

    def __call__(self, z: list) -> list:
        raise NotImplementedError('Need to implement it!')

    def __and__(self, other: 'XenakisObject') -> 'Sieve':
        raise NotImplementedError('Need to implement it!')

    def __or__(self, other: 'XenakisObject') -> 'Sieve':
        raise NotImplementedError('Need to implement it!')


class Residual(XenakisObject):
    """
    Xenakis Residual.
    """

    @staticmethod
    def from_str(residual: str):
        """
        Create a Residual object from a string.
        """
        residual = residual.strip()  # remove trailing whitespaces
        residual = ''.join(_ for _ in list(
            residual) if _ != ' ' and _ != '\n')  # remove whitespace
        # split at the @ symbol to set the modulus and shift
        shift, modulus = list(int(_) for _ in residual.split('@'))
        # return a Residual object for that modulus and shift
        return Residual(shift, modulus)

    def __init__(self, modulus: int = 1, shift: int = 0, neg: bool = False, residuals: list = None):
        """
        Create a Residual from a modulus and shift. `int` only.
        """
        self.modulus = int(modulus)
        self.shift = int(shift) % self.modulus  # normalize the shift
        self.neg = neg  # set if its an inverse sieve
        self.residuals = residuals or [self]

    def __call__(self, z: iter) -> list:
        return self.for_iter(z)

    def __str__(self) -> str:
        """
        Output the Residual as a `str` in the form "MODULUS@SHIFT".
        """
        return f'{"!" if self.neg else ""}{self.modulus}@{self.shift % self.modulus}'

    def __repr__(self) -> str:
        """
        Output the Residual as an `eval()`-ready string.
        """
        return f'Residual(modulus={self.modulus}, shift={self.shift}, neg={self.neg})'

    def for_index(self, n: int) -> bool:
        """
        Check if `n` is a valid value for the Residual.
        """
        res = (
            n - self.shift) % self.modulus == 0  # check if value is valid for the Residual
        return not res if self.neg else res

    def for_iter(self, z: iter) -> list:
        """
        Return a list of values that are valid for a given iterator.
        """
        return list(n for n in z if self.for_index(
            n))  # return a list of valid values for the iterator

    def __and__(self, other: XenakisObject) -> XenakisObject:
        if self.modulus == other.modulus and self.shift == other.shift:
            return Residual(self.modulus, self.shift)

        modulus = self.modulus * other.modulus
        shift = min([self.shift, other.shift])

        max_seek = modulus
        seek = 0
        r = Residual(modulus, shift, residuals=self.residuals + other.residuals)

        while not (
                self.for_index(shift) ==
                other.for_index(shift) ==
                r.for_index(shift)
        ) and seek <= max_seek:
            shift += 1
            r.shift = shift
            seek += 1

        if seek == max_seek:
            raise ValueError('Impossible residual.')

        else:
            return r


if __name__ == '__main__':
    r1 = Residual(1, 7)
    r2 = Residual(3, 1)
    r3 = Residual(7, 3)

    z = range(137)

    rs1, rs2, rs3 = r1(z), r2(z), r3(z)

    print(r1, rs1, r2, rs2, r3, rs3)

    print('  comparison\n--------------')
    for i in z:
        print(f"{i:3d}: {1 if i in rs1 and i in rs2 and i in rs3 else 0} {1 if i in rs1 else 0} {1 if i in rs2 else 0} {1 if i in rs3 else 0}")
    print()

    Rr = r1 & r2 & r3

    print(Rr, Rr(z))
