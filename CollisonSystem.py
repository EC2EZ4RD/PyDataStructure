import math
	
class Particle(object):
	"""docstring for Particle"""
	def __init__(self, rx, ry, vx, vy, mass, radius):
		super(Particle, self).__init__()
		self.rx = rx
		self.ry = ry
		self.vx = vx
		self.vy = vy
		self.mass = mass
		self.radius = radius
		self.count = 0

	def move(self, dt):
		if rx+vx*dt < radius or rx+vx*dt > 1 - radius:
			vx = -vx
		if ry+vy*dt < radius or ry+vy*dt > 1 - radius:
			vy = -vy
		rx = rx + vx * dt
		ry = ry + vy * dt

	def timeToHit(self, that):
		if self == that:
			return float('inf')
		dx = self.rx - that.rx
		dy = self.ry - that.ry
		dvx = self.vx - that.vx
		dvy = self.dvy - that.dvy
		dvdr = dx*dvx + dy*dvy
		if dvdr >= 0:
			return float('inf')
		dvdv = dvx*dvx + dvy*dvy
		drdr = dx*dx + dy*dy
		sigma = self.radius + that.radius
		d = (dvdr*dvdr)-dvdv*(drdr-sigma*sigma)
		if d < 0:
			return float('inf')
		return -(dvdr + math.sqrt(d))/dvdv
	
	def timeToHitVerticalWall(self):
		pass

	def timeToHitHorizontalWall(self):
		pass
	
	def bounceOff(self, that):
		dx = self.rx - that.rx
		dy = self.ry - that.ry
		dvx = self.vx - that.vx
		dvy = self.dvy - that.dvy
		dvdr = dx*dvx + dy*dvy
		dist = self.radius + that.radius
		J = 2 * self.mass + that.mass * dvdr / ((self.mass + that.mass)*dist)
		Jx = J * dx / dist
		Jy = J * dy / dist
		self.vx += Jx / self.mass
		self.vy += jy / self.mass
		that.vx -= Jx / that.mass
		that.vy -= jy / that.mass
		self.count += 1
		that.count += 1

	def bounceOffVerticalWall(self):
		pass

	def bounceOffHorizontalWall(self):
		pass

class Event(object):
	"""docstring for Event"""
	def __init__(self, time, a, b):
		super(Event, self).__init__()
		self.time = time
		self.a = a
		self.b = b

	def compareTo(self, that):
		return self.time - that.time

	def isValid():
		if a == b:
			return False
		dx = a.rx - b.rx
		dy = a.ry - b.ry
		dvx = a.vx - b.vx
		dvy = a.dvy - b.dvy
		dvdr = dx*dvx + dy*dvy
		if dvdr >= 0:
			return False
		dvdv = dvx*dvx + dvy*dvy
		drdr = dx*dx + dy*dy
		sigma = a.radius + b.radius
		d = (dvdr*dvdr)-dvdv*(drdr-sigma*sigma)
		if d < 0:
			return False
		return True

class CollisionSystem(object):
	"""docstring for CollisionSystem"""
	def __init__(self, particles, pq = MinPQ([]), t = 0):
		super(CollisionSystem, self).__init__()
		self.particles = particles
		self.pq = pq
		self.t = t

	def predict(a):
		if a == None:
			return;
		for i in range(len(self.particles)):
			dt = a.timeToHit(self.particles[i])
			self.pq.insert(Event(t+dt, a, i))
		self.pq.insert(Event(t + a.timeToHitHorizontalWall, None, a))
		self.pq.insert(Event(t + a.timeToHitVerticalWall, a, None))

	def simulate():
		self.pq = MinPQ([])
		for particle in self.particles:
			self.predict(particle)
		self.pq.insert(Event(0, None, None))

		while self.pq.isEmpty() == False:
			event = self.pq.delMin()
			if event.isValid() == False:
				continue
			a = event.a
			b = event.b
		for particle in self.particles:
			particle.move(event.time - self.t)
		self.t = event.time

		if a != None and b != None:
			a.bounceOff(b)
		elif a != None and b != None:
			a.bounceOffVerticalWall()
		elif a != None and b != None:
			a.bounceOffHorizontalWall()
		else:
			self.redraw()

		self.predict(a)
		self.predict(b)