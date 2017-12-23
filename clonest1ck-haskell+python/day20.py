class Particle(object):
    def __init__(self, p, v, a, i):
        self.p = p
        self.v = v
        self.a = a
        self.d = p.manhattan()
        self.id = i

    def update(self):
        self.v.add(self.a)
        self.p.add(self.v)
        self.d = self.p.manhattan()

    def __str__(self):
        return "Particle at " + str(self.p) + ", v = " + str(self.v) + ", a = " + str(self.a)

    def __cmp__(self, p2):
        return self.d - p2.d

class Vector3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v2):
        self.x += v2.x
        self.y += v2.y
        self.z += v2.z

    def manhattan(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __eq__(self, v2):
        return (self.x == v2.x) and (self.y == v2.y) and (self.z == v2.z)


def Task1(particles):
    particles.sort()
    first = particles[-1]

    while(first.__cmp__(particles[0]) != 0):
        first = particles[0]
        for i in range(1000):
            for particle in particles:
                particle.update()
        particles.sort()

    return first.id

def Task2(particles):
    loopsSinceLastIncident = 0
    while(loopsSinceLastIncident < 1000):
        for particle in particles:
            particle.update()
        i = 0
        start = 0
        while(i < len(particles) - 1):
            if(particles[i].p.__eq__(particles[i+1].p)):
                loopsSinceLastIncident = -1
                start = i
                i += 1
                while(i < len(particles) - 1 and particles[i].p == particles[i+1].p):
                    i += 1
                particles = particles[:start] + particles[i+1:]
                i = start - 1
            i += 1
        loopsSinceLastIncident += 1
    return len(particles)

f = open("in20.txt", 'r')
particles = []
i = 0

for line in f.readlines():
    line = [x.split("=")[1].split("<")[1].split(">")[0].split(",") for x in line.split("\n")[0].split(", ")]
    pos = [int(x) for x in line[0]]
    vel = [int(x) for x in line[1]]
    acc = [int(x) for x in line[2]]

    pos = Vector3(pos[0], pos[1], pos[2])
    vel = Vector3(vel[0], vel[1], vel[2])
    acc = Vector3(acc[0], acc[1], acc[2])

    par = Particle(pos, vel, acc, i)
    particles.append(par)
    i += 1


print "Task 1: " + str(Task1(particles[:]))
print "Task 2: " + str(Task2(particles[:]))
