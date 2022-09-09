# -*- coding: utf-8 -*-
"""
@author: Edward Chang
"""

#one dimensional linear (non-radial) Schrodinger equation
#finding wave function for test eigenenergy
#units: length in angstroms, energy in eV, mass in electron masses

import numpy as np
import matplotlib.pyplot as plt

alpha = 1. #eV/A
def V(x): #potential (energy)
    if x < 0:
        return 1e99
    else:
        return alpha*x

startx = 0. #probably don't change this
endx = 20.

E = 3.65171  #eV (eigenenergy guess)
beta = .26246 #eV^-1*A^-2 for a one-electron mass (2m/hbar**2)

psi0 = 0. #initial value of wave function
first_psi0 = 1. #initial value of first derivative of wave function
second_psi0 = beta*(V(startx) - E)*psi0 #initial second derivative

dx = .0005 #A (step size)

psi_ara = np.array([])  #arrays to be filled and used for plotting
psi_ara = np.append(psi_ara,psi0)  #filling with initial values
first_psi_ara = np.array([])  #first and second will denote derivatives
first_psi_ara = np.append(first_psi_ara,first_psi0)
second_psi_ara = np.array([]) #from here on out
second_psi_ara = np.append(second_psi_ara,second_psi0)

x = startx  #setting up x with its array to plot later
x_ara = np.array([])
x_ara = np.append(x_ara,startx)

V_ara = np.array([])  #to plot potential vs x
V_ara = np.append(V_ara,V(startx))
E_ara = np.array([])  #for energy vs x
E_ara = np.append(E_ara,E)

old_psi = psi0  #"old" values will be used in the while loop
old_first_psi = first_psi0  #to find "new" values
old_second_psi = second_psi0

while x < endx:  #the meat of the code
    new_psi = old_psi + old_first_psi*dx + old_second_psi*dx**2/2.
    new_first_psi = old_first_psi + old_second_psi*dx
    new_second_psi = beta*(V(x + dx) - E)*new_psi
    
    psi_ara = np.append(psi_ara,new_psi)  #append values to arrays
    first_psi_ara = np.append(first_psi_ara,new_first_psi)
    second_psi_ara = np.append(second_psi_ara,new_second_psi)
    
    old_psi = new_psi  #setting up for the next loop
    old_first_psi = new_first_psi
    old_second_psi = new_second_psi
    
    x += dx  #increment x
    x_ara = np.append(x_ara,x)
    
    V_ara = np.append(V_ara,V(x))  #making potential array
    E_ara = np.append(E_ara,E)  #making energy array

fig,ax = plt.subplots()  #plotting psi, V, and E
ax.plot(x_ara,V_ara,'g')
ax.plot(x_ara,psi_ara,'r')
ax.plot(x_ara,E_ara,'b')
ax.set(title='psi vs x (green is potential in Joules, blue is energy of particle in Joules)', xlabel='x (A)', ylabel='psi')
ax.set_ylim(-6.,12.)
ax.grid()
plt.show()
