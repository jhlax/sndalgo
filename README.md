# `sndalgo`<span>&ndash;</span>signal / number stuff for creative use


20 nov 2019 | __John Harrington__

## installation

20 nov 2019 | __John Harrington__

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



