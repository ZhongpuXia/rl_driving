"""
"""

from dynamics import Dynamics

class Vehicle(Dynamics):
	
	def dynamics(self, state, t, action):
		"""
		Motion Dynamics of vehicle
		@Parameter
		state: numpy array including
			-px: position x
			-py: position y
			-vx: veolcity x
			-vy: velocity y
			-theta: heading angle
			-omega: heading angle velocity
		t: time numpy arrray
		action: numpy array including
			-acc: acceleration of the vehicle
			-omega: heading angle velocity
		"""
		px, py, vx, vy, theta, omega = state
		acc, omega = action
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

