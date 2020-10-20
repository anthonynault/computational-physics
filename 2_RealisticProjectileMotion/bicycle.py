import matplotlib.pyplot as plt


def speedUp(airDrag=False):
    v = 0
    t = 0
    velocity = [v]
    time = [t]
    totalTime = 200
    timeStep = .05
    timeSteps = xrange(int((totalTime / timeStep)) - 1)
    power = 400
    mass = 70
    airDensity = 1
    surfaceArea = 0.33
    dragAcceleration = 0
    powerAcceleration = 0
    force = float(power) / 7

    for i in timeSteps:

        if force * v < power:
            # bike is accelerating from rest with constant force
            powerAcceleration = float(force / mass)

        else:
            powerAcceleration = float(power) / (mass * v)

        if airDrag:
            dragAcceleration = float(airDensity * surfaceArea * v * v) / (2 * mass)

        # calculate velocity
        v += (powerAcceleration - dragAcceleration) * timeStep
        t += timeStep

        # store results
        time.append(t)
        velocity.append(v)

    plt.plot(time, velocity)
    plt.ylabel("velocity (m/s)")
    plt.xlabel("time (s)")
    plt.title("Bicycle Velocity")
    plt.savefig('velocity.png', bbox_inches='tight')


if __name__ == '__main__':
    speedUp(airDrag=True)
