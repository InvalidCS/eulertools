
def isprime(n: int) -> bool:
    '''Checks n for primality using BPSW.'''
    if n<=1:
        return False
    for i in [2,3,5,7,11,13,17,19,23,29]:
        if n%i == 0:
            if n/i == 1:
                return True
            else:
                return False
    #Applying Miller-Rabin base 2
    a=2
    d=n-1
    s=0
    while(d%2==0):
        d=int(d/2)
        s+=1
    if not (a**d)%n == 1:
        for r in range(s):
            print(r)
            if (a**(d*2**r))%n==(-1)%n:
                break
            elif r==s-1:
                return False
    return True

  #Identical to tdiv. This is here for now since it runs faster than the above.
##def isprime(n) -> bool:
##    '''Performs trial division to determine primality.'''
##    if n<0:
##        raise ValueError('Negative number received')
##    elif n<2:
##        return False
##    for i in range(2,int(n**(1/2))+1):
##        if n%i == 0:
##            return False
##    return True

def tdiv(n) -> bool:
    '''Performs trial division to determine primality.'''
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def nextprime() -> int:
    '''Yields the next prime, starting with 2.'''
    yield 2
    pl = []
    x = 3
    while True:
        possprime = True
        lim = x**(1/2)
        for i in pl:
            if i>lim:
                break
            if x%i == 0:
                possprime = False
                break
        if possprime:
            pl.append(x)
            yield x
        x += 2

def genprimes(n) -> int:
    '''Yields all primes less than or equal to n. Will return nothing if n<2.'''
    if n < 2:
        return
    if n == 2:
        yield 2
        return
    yield 2
    pl = []
    for x in range(3,n+1,2):
        possprime = True
        lim = x**(1/2)
        for i in pl:
            if i>lim:
                break
            if x%i == 0:
                possprime = False
                break
        if possprime:
            pl.append(x)
            yield x

def genprimelist(n) -> list:
    '''Returns a list of all primes less than or equal to n.'''
    if n < 2:
        return []
    if n == 2:
        return [2]
    pl = []
    for x in range(3,n+1,2):
        possprime = True
        lim = x**(1/2)
        for i in pl:
            if i>lim:
                break
            if x%i == 0:
                possprime = False
                break
        if possprime:
            pl.append(x)
    return [2]+pl
            

def pfac(n) -> list:
    '''Returns the prime factorization of n.'''
    if n<2:
        return []
    z=2
    lim = n**(1/2)
    pfacs=[]
    hasfactors=True
    while hasfactors:
        if(n%z==0):
            pfacs.append(z)
            n=n/z
        elif z+1>lim:
            hasfactors=False
            if not n==1:
                pfacs.append(int(n))
        else:
            z+=1
    return pfacs

def spfac(n) -> list:
    '''Returns the prime factorization of n as a set.'''
    if n<2:
        return []
    z=2
    lim = n**(1/2)
    pfacs=set()
    hasfactors=True
    while hasfactors:
        if(n%z==0):
            pfacs.add(z)
            n=n/z
        elif z+1>lim:
            hasfactors=False
            if not n==1:
                pfacs.add(int(n))
        else:
            z+=1
    return pfacs

if __name__ == '__main__':
    from timer import Timer
    g = genprimes(10000000)
    t = Timer()
    t.start()
    for _ in g:
        pass
    t.stop()
    print(t.read_str())
    while True:
        try:
            n=int(input())
            print(isprime(n))
        except ValueError:
            print('Invalid n')
