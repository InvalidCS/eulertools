def divisors(n:int) -> list:
    '''Returns the divisors of n.'''
    div=[]
    for i in range(1,n//2+1):
        if n%i==0:
            div.append(i)
    div.append(n)
    return div

def pdivisors(n:int) -> list:
    '''Returns the proper divisors of n.'''
    div=[]
    for i in range(1,n//2+1):
        if n%i==0:
            div.append(i)
    return div

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
            lim = n**(1/2)
        elif z+1>lim:
            hasfactors=False
            if not n==1:
                pfacs.add(int(n))
        else:
            z+=1
    return pfacs

def gcf(a, b) -> int:
    '''Returns the greatest common factor of a and b.'''
    if a<b:
        t = a
        a = b
        b = t
    while not a%b == 0:
        a = a%b
        if a<b:
            t = a
            a = b
            b = t
    return b

def totient(n) -> int:
    '''Returns the number of numbers less than n
    that are relatively prime to n.'''
    if n == 1:
        return 1
    pf_set = spfac(n) #All items except last one
    t = 1
    for pf in pf_set:
        if not pf == n:
            t *= 1-1/pf
    if not t == 1:
        t *= n
    else:
        t = n-1
    return int(t)

def c(n, prelist, pfact=-1.2487) -> list:
    '''Iterates through all factor combinations of n, yielding one at a time.
    The prelist and pfact arguments are primarily for recursive use and should
    be left blank by the user.'''
    if pfact==-1.2487:
        pfact = pfac(n)
    pdivs = pdivisors(n)
    try:
        rootfac = [pdivs[1], int(n/pdivs[1])]
    except:
        return
    yield prelist+rootfac
    for i in range(2,len(pdivs)//2+1):
        currfac = [pdivs[i], int(n/pdivs[i])]
        yield prelist+currfac
    if not prelist+rootfac == pfact:
        h=c(int(n/pdivs[1]), prelist+[pdivs[1]], pfact)
        for cf in h:
            yield cf
        for i in range(2,len(pdivs)//2+1):
            currfac = [pdivs[i], int(n/pdivs[i])]
            h=c(int(n/pdivs[i]), prelist+[pdivs[i]], pfact)
            for cf in h:
                yield cf

if __name__ == '__main__':
    print(gcf(69,81))
    
        
    
    
