# !/usr/bin/env python

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def vehicle(state, t, acc):
	px = state[0]
	py = state[1]
	vx = state[2]
	vy = state[3]
	theta = state[4]
	omega = state[5]
	d_px = vx
	d_py = vy
	d_vx = -omega * vy + acc * np.cos(theta)
	d_vy = omega * vx + acc * np.sin(theta)
	d_theta = omega
	if np.cos(theta) < 0.5:
		d_omega = acc * omega * np.sin(theta) / vy
	else:
		d_omega = acc * omega * np.cos(theta) / vx
	return [d_px, d_py, d_vx, d_vy, d_theta, d_omega]

state0 = [1, 0, 0, 1, np.pi / 2, 1]
t1 = np.linspace(0, 1 * np.pi, 100)
sol1 = odeint(vehicle, state0, t1, args=(0.1,))

new_state0 = sol1[-1, :]
t2 = np.linspace(t1[-1], 6, 100)
new_state0[5] = 0
sol2 = odeint(vehicle, new_state0, t2, args=(0,))

sol = np.vstack((sol1, sol2))
t = np.hstack((t1, t2))

xs = sol[:, 0]
ys = sol[:, 1]
vs = np.sqrt(sol[:, 2]**2 + sol[:, 3]**2)
omegas = sol[:, 5]
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
