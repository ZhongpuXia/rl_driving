# !/usr/bin/env python

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def vehicle(state, omega):
    px = state[0]
    py = state[1]
    vx = state[2]
    vy = state[3]
    theta = state[4]
    d_px = vx
    d_py = vy
    d_vx = -omega * vy 
    d_vy = omega * vx
    d_theta = omega
    return [d_px, d_py, d_vx, d_vy, d_theta]

state_0 = [1, 0, 0, 1, np.pi / 2]
t = np.linspace(0, 2 * np.pi, 100)
sol = odeint(vehicle, state_0, t, args=(1))

xs = sol[:, 0]
yx = sol[:, 1]
plt.plot(xs, ys, '.r')
plt.show()
