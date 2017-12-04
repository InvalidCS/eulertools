def nexttri():
    '''Yields next triangular number.'''
    n = 1
    while True:
        yield int(n*(n+1)/2)
        n += 1

def nextsq():
    '''Yields next square number.'''
    n = 1
    while True:
        yield n**2
        n += 1

def nextpent():
    '''Yields next pentagonal number.'''
    n = 1
    while True:
        yield int(n*(3*n-1)/2)
        n += 1

def nexthex():
    '''Yields next hexagonal number.'''
    n = 1
    while True:
        yield n*(2*n-1)
        n += 1

def nexthept():
    '''Yields next heptagonal number.'''
    n = 1
    while True:
        yield int(n*(5*n-3)/2)
        n += 1

def nextoct():
    '''Yields next octagonal number.'''
    n = 1
    while True:
        yield n*(3*n-2)
        n += 1

def gen(n: int):
    '''Returns a generator for the specified series.'''
    if n == 3:
        return nexttri()
    elif n == 4:
        return nextsq()
    elif n == 5:
        return nextpent()
    elif n == 6:
        return nexthex()
    elif n == 7:
        return nexthept()
    elif n == 8:
        return nextoct()
    else:
        raise ValueError('No series for n = '+str(n))

def memberof(x, n) -> bool:
    '''Returns whether x is a member of the nth figurate series.'''
    if n == 3:
        return istri(x)
    elif n == 4:
        return issq(x)
    elif n == 5:
        return ispent(x)
    elif n == 6:
        return ishex(x)
    elif n == 7:
        return ishept(x)
    elif n == 8:
        return isoct(x)
    else:
        raise ValueError('No series for n = '+str(n))

def istri(x) -> bool:
    '''Returns whether x is triangular.'''
    return (((8*x+1)**(1/2)-1)/2)%1 < 0.00000000001

def issq(x) -> bool:
    '''Returns whether x is square.'''
    return (x**(1/2))%1 < 0.00000000001

def ispent(x) -> bool:
    '''Returns whether x is pentagonal.'''
    return (((24*x+1)**(1/2)+1)/6)%1 < 0.00000000001

def ishex(x) -> bool:
    '''Returns whether x is hexagonal.'''
    return (((8*x+1)**(1/2)+1)/4)%1 < 0.00000000001

def ishept(x) -> bool:
    '''Returns whether x is heptagonal.'''
    return (((40*x+9)**(1/2)+3)/10)%1 < 0.00000000001

def isoct(x) -> bool:
    '''Returns whether x is octagonal.'''
    return (((3*x+1)**(1/2)+1)/3)%1 < 0.00000000001


