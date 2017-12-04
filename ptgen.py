def nexttriple() -> tuple:
    '''Yields the next pythagorean triple as a tuple (a, b, c).'''
    p = 2
    while True:
        for q in range(p-1,0,-1):
            #p and q cannot both be odd or both even
            if p%2 == 1 and q%2 == 1:
                continue
            if p%2 == 0 and q%2 == 0:
                continue
            a = p*q*2
            b = p**2 - q**2
            c = b + 2*q**2
            yield [a,b,c]
        p += 1

def nexttripleab() -> tuple:
    '''Yields just the a and b values for the next triple.'''
    p = 2
    while True:
        for q in range(p-1,0,-1):
            #p and q cannot both be odd or both even
            if p%2 == 1 and q%2 == 1:
                continue
            if p%2 == 0 and q%2 == 0:
                continue
            a = p*q*2
            b = p**2 - q**2
            c = b + 2*q**2
            if a<=b:
                yield (a,b)
            else:
                yield (b,a)
        p += 1
