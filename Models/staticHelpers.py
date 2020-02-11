def printProgress(i, iterations_per_dot):
    if i > 0 and i % iterations_per_dot == 0:
        if i % (50 * iterations_per_dot) == 0:
            print("\n")
        print(".", end='')
