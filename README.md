# quantum-eigenenergies-for-one-dimensional-potentials

Some code that can be used to approximate energy states for a particle in a one-dimensional potential using Python and Matplotlib

## Overview
Each time the code is run, a plot will be shown which approximates a wave function associated with a certain energy in the given potential.

If the potential function is a well, increasing more as distance "x" from zero increases, the resulting wave function is expected to diminish at large x. This fact can be utilized to test more and more accurate eigenenergies and deduce whether a tested eigenenergy is too large or too small for a state, since the approximate wave functions generated from the code do not diminish at large x.

The potential is stored in the function V(x) for positive x, and the potential is infinity for negative x.

## Example
By default the potential is set to alpha\*x.

Once the starting parameters are set, the first energy level should look like one hump and then an asymptotic tail at large x. The direction of the tail is an indicator showing whether the test energy was too high or too low for the closest energy level.

With this information, more and more precise energies wave functions can be guessed and produced in order to pinpoint a specific energy to a desired number of significant digits.

The first non-trivial energy for the default potential is 3.6517 eV.