
def main():
    fall()
    fallWithDrag()


def fall(v=0, time=100):
    dt = .05
    nsteps = int(time / dt) - 1

    for i in xrange(nsteps):
        v += 9.8 * dt
        print(i, v)


def fallWithDrag(v=0, time=20):
    dt = .05
    nsteps = int(time / dt) - 1

    for i in xrange(nsteps):
        v += (9.8 - v) * dt
        print (i, v)


if __name__ == '__main__':
    main()
