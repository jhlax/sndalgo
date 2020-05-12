class Voltage:
    volts = 0


class Capacitance:
    farads = 0


class Resistance:
    ohms = 0


class Inductance:
    henries = 0


class Node:
    connections = {}


class Component(Node):
    pass


class Resistor(Component, Resistance):
    pass


class Capacitor(Component, Capacitance):
    pass


class Inductor(Component, Inductance):
    pass


class Current:
    AC = 0
    DC = 1

    _voltage = None
    _resistance = None

    c_type = DC

    @property
    def amperes(self):
        try:
            if self.resistance == 0 and self.voltage:
                raise Exception("<Short circuit>")
            return self.resistance / self.voltage
        except ZeroDivisionError:
            raise Exception("<No voltage>")

    @property
    def voltage(self):
        if self._voltage is None:
            return 0

        else:
            return self._voltage

    @property
    def resistance(self):
        if self._resistance is None:
            return 0

        else:
            return self._resistance


class Source(Component):
    function = lambda t: 3.3  # 3.3 volts default


class VoltageSource(Component, Voltage):
    pass


class CurrentSource(Component, Current):
    pass


class Ground(Component):
    connections = {}


class Wire(Current):
    source = None
    terminal = None

    def __init__(self, i, o=None):
        if o is None:
            o = Ground

        self.source = i
        self.terminal = o

    @property
    def positive(self):
        return self.terminal

    @property
    def negative(self):
        return self.source

    @property
    def v_out(self):
        return self.terminal

    @property
    def v_in(self):
        return self.source


a = Wire(CurrentSource())

print(a.v_in.amperes)