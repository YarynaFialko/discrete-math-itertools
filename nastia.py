	def combinations(r, n):
    if r>n:
        return
    ourange=[i for i in range(r)]
    yield tuple(i for i in ourange)
    while True:
        y=0
        for i in reversed(range(r)):
            if ourange[i] != i + n - r:
                y=1
                break
        if y==0:
            return
        ourange[i] += 1
        for j in range(i+1, r):
            ourange[j] = ourange[j-1] + 1
        yield tuple(i for i in ourange)
