# UX

the ux has to be different for a few use-cases:

1. direct use via *command line*
3. **command** line to *file*
3. **file** to *command line*
3. **piping files** streams in command line
7. piping data from one executable to the other *composably*
7. a **single** application to perform all of this
7. `.wav` file input *and* output
7. `midi` input *and* output (with file support)
7. real-time systems; *AOT* compilation
7. time-domain algorithms
7. ***analysis overkill***

the command line and functions must be reciprocal, all units in this
module must be coherent, with a single purpose and portability

## common themes so far

how information is piped always needs a separator of `' '` in order to
function correctly in argument-less cases

units and time based information is both *stateful* and should also
be *dynamic*

standardize the variable names in the source for key terms

commands can be easily split and piped... until we need to have
concurrent processes; multiprocessing and asynchronous methods can be
beneficial

a sort of syntactical string that defines larger blocks of these
components in their structured form, usable as a whole

we need to have more conversions. we also need context management for
many areas
