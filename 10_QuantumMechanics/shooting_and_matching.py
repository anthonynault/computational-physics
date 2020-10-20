
def main():
    totalSpace = 4
    spatialStep = .01
    spatialSteps = xrange((totalSpace / spatialStep) - 1)
    energy = 1
    energyStep = .05
    psiValues = [0, 0]  # initialize for even pairity solutions
    lastDiverge = 0  # track the direction of the diverging trend

    #  initialize the potentia well energy
    potentialValues = [0 if x >= 0 and x <= 2 else 100 for x in spatialSteps]



    for i in spatialSteps:
        psi = 2 * psiValues[i] - psiValues[i-1] - 2 * (energy - 0)








if __name__ == '__main__':
    main()
