from math import sqrt
from math import pow
from math import hypot
import matplotlib.pyplot as plt


def main():

    x = 0  # x position
    y = 0  # y position
    v_x = 50  # x velocity
    v_y = 50  # y velocity
    v = 0  # net velocity
    m = 1  # mass
    positions = []
    velocities = []
    positions.append((x, y))
    velocities.append((v_x, v_y))
    B = .00004
    g = 9.8  # acceleration due to gravity
    dt = .05

    while True:
        v = hypot(v_x, v_y)
        x += v_x * dt
        y += v_y * dt
        v_x -= ((B * v * v_x) / m) * dt
        v_y -= (g + ((B * v * v_y) / m)) * dt

        positions.append((x, y))
        velocities.append((v_x, v_y))

        if y <= 0:
            break

    x = [i[0] for i in positions]
    y = [i[1] for i in positions]

    plt.plot(x, y)
    plt.ylabel("y position (m)")
    plt.xlabel("x position (m)")
    plt.title("Projectile Motion")
    plt.savefig('projectile.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
