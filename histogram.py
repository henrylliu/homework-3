def histogram(points, bins):
    """
    Returns a python list which contains the density within each bin of the histogram
    Input:
        - points (list): Sorted python list of numbers from smallest to largest
        - bins (list): List of k tuples where we are given [start, end)
    Return:
        - densities (list): List of 
    """
    n = len(points)
    k = len(bins)

    densities = [0] * k
    total = point = bin = 0

    while point < n and bin < k:
        start, stop = bins[bin]
        # Smaller than bin start point
        if points[point] < start:
            point += 1
        # Go to next point, greater than current bin endpoint
        elif points[point] >= stop:
            bin += 1
        # Add count to current bin, increment total by one
        else:
            densities[bin] += 1
            point += 1
            total += 1
    print(total)
    for i in range(k):
        start, stop = bins[i]
        densities[i] /= (total * (stop - start))
    return densities