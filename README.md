# `sndalgo`<span>&ndash;</span>signal / number stuff for creative use

20 nov 2019 | __John Harrington__

## installation

1. clone this repository
2. install `pipenv`

   `pip3 install pipenv`
3. enter and set up environment

   `cd sndalgo`

   `pipenv install`
4. enter the environment shell

   `pipenv shell`
5. write code!

   `vim fuck.py`

## scripts and preparing the module

so, this repo has not been set up to be a package that can be installed thru `pip`, *but*
it can be emulated with this... at least NOT on windows ;)

which means this is for **mac** and linux (either through .profile or not) only

so what i would do is first:

1. figure out the clone path. for me its `~/projects/sndalgo`.
2. add that to your `PYTHONPATH` with this command:

   `echo "export PYTHONPATH=$PYTHONPATH:~/projects/sndalgo" >> ~/.bash_profile`

3. then add the scripts folder for that clone path (`$HOME/projects/sndalgo/scripts` for me) to your `PATH`:

   `echo "export PATH=$PATH:$HOME/projects/sndalgo/scripts" >> ~/.bash_profile`

> as you can see, `~` and `$HOME` are equivalent here. and i did `git clone <this repo>` in my ~/projects folder to create `~/projects/sndalgo`.

### scripts available / usable

there are a few scripts available:

1. `sieve`
2. `pnote`
3. `modulus`

and when using them together with pipes, i recommend (because it works) to use the `-s ' '` flag at the beginning, which outputs them as *space-delimited* integers.

#### `sieve`

try using `sieve` in your terminal after closing and reopening it (so the `.bash_profile` refreshes, OR by using `source ~/.bash_profile` in an active terminal).

specifically, try `sieve --help` first to see the shit.

`Z_RANGE` is the arguments for python's `range()` function separated by spaces.

`SIEVE_STR` is essentially a ***double quoted string*** that contains residuals, combined with logic operators. i.e. `-- "-3@2 & 4 | -3@1 & 4@2 | 3 & 4@2"`. notice the `--` before, with a space, which will denote that the `-` symbols in the double-quoted string are not arguments to the CLI program.

#### `pnote`

`pnote` outputs a number as it's human-readable key/octave/cents form...

i.e.

```
pnote -s ' ' 0 1 2
```

will result in

```
C-1 C#/Db-1 D-1
```

or an easy one is

```
pnote -s ' ' 69 82
```

```
A4 A5
```

#### `modulus`

modulus takes, again, another space delimited string of integers and outputs them at modulus 12
(with option `-m MODULUS` to change that)

```
modulus -s ' ' 13 14 15 16
```

to

```
1 2 3 4
```

or

```
modulus -m 7 -s ' ' 13 14 15 16
```

to

```
6 0 1 2
```

## `xenakis`

our xenakis sieve package. this will be extremely integrated into
this system.

### reasoning

1. xenakis sieves extend a form of set theory that is constructable
and manipulable with logical operations (i.e. `AND`, `OR`).
2. sieves have a dual ability to operate as both _CV_ and _signal_
parameters, depending on how they are used.
3. applications like step sequencers, theory guides, and
sidechainers are all summated within a single body of knowledge.
4. algorithmic composition.
5. synthesis, analysis, and architecture of composition with
scales, chords, progressions, order, and any other hand in building
sonic phenomena.
6. modular design, dimensionless, unitless.

### usage

```python
from sndalgo.xenakis import Sieve

major_scale = Sieve('-3@2&4|-3@1&4@1|3@2&4@2|-3@0&4@3')
notes = major_scale.set(range(0,25))

ots = Sieve('1@7') & '3@1' & (7, 3, False)

print(major_scale, major_scale.simple, notes)
```

## `pitch`

_<span style="color:red;">planning</span>_

this can convert pitches to frequencies, integers to pitches;
anything that needs conversion, normalization, etc. should be found
here.

### uses

1. conversion between different units with frequency-domain
2. analyzing, creating, and applying scales
3. transforming numbers into time-domain values

## `midi`

_<span style="color:red;">planning</span>_

this should have both real-time and hard-bodied MIDI utilities.

### uses

1. forming `.mid` files from inputs
2. reading `.mid` files and exposing an API for them
3. analyzing MIDI
4. streaming (duplex) MIDI (hopefully) without dependencies



# notes

alright. it seems like we want to have a dynamically allocated input of values in a sequence for nearly all of our functions.

this sequence can be a sieve's resolution or translated midi, etc. etc.

there is the `sample rate`, the `separator`, `frequency`, `block size`, `harmonics`...

* `modulus`
* `notes`
* `z range`
* `sieve`
* `output format`

so we have a quick few things to relate properly, and study for compilability and interoperability.

a good aim is to create a simple eco system of files and types to be commandable with one `click` command script (although with multiple features etc. etc.)

we need utilities like:

* the multiple formats for sieves should be implemented
* files **AND** stdin streams for pipes
* bash and python scriptable and with a common api
* reverse, shrink, expand, etc. for sequencing
* operations
* filetypes that are standardized
* more cowbell

over time, this will be a huge tool for synthesis and processing of sound. hopefully.

