#!/usr/bin/env python3

"""
sieve / sieve utilities
"""

__author__ = 'John Harrington'
__version__ = '1.0.0'

import click
import sndalgo


@click.command()
@click.argument('sieve_str', type=str)
@click.argument('z_range', nargs=-1, type=int)
@click.option('--sep', '-s', type=str, help='the separator for the output', default='\n')
@click.option('--simple', '-S', is_flag=True, default=False, help='use or output the simplified sieve')
@click.option('--fmt', '-f', type=click.Choice(['set', 'unit', 'delta', 'bin'], case_sensitive=False), default='set')
def sieve(sieve_str, z_range, sep, simple, fmt):
    s = sndalgo.Sieve(sieve_str)
    out_str = 'sieve:'

    if simple:
        s = s.simple
        out_str = '(simplified) ' + out_str

    if len(z_range):
        z = range(*z_range)

    else:
        print(s.stype, out_str, s)
        exit(0)

    fmt = fmt.lower()

    r = getattr(s, fmt)(z)

    print(*r, sep=sep)


if __name__ == '__main__':
    sieve()
