# !/usr/bin/env python

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from vehicle import Vehicle

state0 = [1, 0, 0, 1, np.pi / 2, 1]
t1 = np.linspace(0, 1 * np.pi, 100)
veh = Vehicle(state0, period=0.1)
states1 = np.zeros((len(t1), len(state0)))
for i, t in enumerate(t1):
	states1[i] = veh.step(0.1)

t2 = np.linspace(t1[-1], 6, 100)
states2 = np.zeros((len(t2), len(state0)))
for i, t in enumerate(t2):
	states2[i] = veh.step((0.0, 0.0))

states = np.vstack((states1, states2))
t = np.hstack((t1, t2))

xs = states[:, 0]
ys = states[:, 1]
vs = np.sqrt(states[:, 2]**2 + states[:, 3]**2)
omegas = states[:, 5]
plt.subplot(311)
plt.plot(xs, ys, '.r')
plt.axis('equal')
plt.title('position of the point')

plt.subplot(312)
plt.plot(t, vs)
plt.title('velocity')

plt.subplot(313)
plt.plot(t, omegas)
plt.title('angle velocity')
plt.show()
