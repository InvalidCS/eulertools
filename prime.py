'''
Author: Christopher DiPalma
Description: A collection of functions related to primality, including a fast isprime function (still could use some work)
and some prime factorization methods.
'''

one_and_two_digit_prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def modpow(base: int, exp: int, mod: int) -> int:
    '''Returns (base**exp)%mod. Slower than built-in pow.'''
    s = bin(exp)[2:]
    s = s[::-1]
    result = 1
    a = base%mod
    for char in s:
        if char == '1':
            result = (result*a)%mod
        a = (a**2)%mod
    return result

def miller_rabin(n: int, a: int) -> int:
    '''Returns False if n is composite, True if it is
    probably prime according to the Miller-Rabin test base a.'''
    d=n-1
    s=0
    while d%2==0:
        d //= 2
        s+=1
    g = pow(a,d,n)
    if not g == 1 or g == n-1:
        z = (-1)%n
        for r in range(1,s):
            g = (g**2)%n
            if g%n==z:
                break
            elif r==s-1:
                return False
    return True

def jacobi(m: int, n: int) -> int:
    if n == 1:
        return 1
    result = 1
    if m < 0:
        m = -m
        result *= _j_neg(n)
    m = m%n
    if m == 0:
        return 0
    if _gcf(m,n) > 1:
        return 0
    if m%2 == 0:
        s = 0
        while m%2 == 0:
            m //= 2
            s += 1
        if not s%2 == 0:
            result *= _j_two(n)
    while not m == 1:
        if m%4 == 3 and n%4 == 3:
            result *= -1
        t = m
        m = n%m
        n = t
        if m%2 == 0:
            s = 0
            while m%2 == 0:
                m //= 2
                s += 1
            if not s%2 == 0:
                result *= _j_two(n)
    return result

def _gcf(a, b) -> int:
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

def _j_two(n: int) -> int:
    '''Returns (2|n).'''
    if n%8 == 1 or n%8 == 7:
        return 1
    else:
        return -1

def _j_neg(n: int) -> int:
    '''Returns (-1|n).'''
    if n%4 == 1:
        return 1
    else:
        return -1

def lucasprime(n) -> bool:
    '''Applies a Lucas prime test.'''
    #Special case
    if n == 2:
        return True
    if _issq(n):
        return False
    D = 5
    while not jacobi(D,n) == -1:
        if D>0:
            D += 2
            D *= -1
        else:
            D *= -1
            D += 2
    P = 1
    Q = (1-D)//4
    Qk = Q
    Uk = 1
    Vk = P
    k = 1
    binexp = bin(n+1)[3:]
    oldl = len(binexp)
    binexp = binexp.rstrip('0')
    diffl = oldl-len(binexp)
    for char in binexp:
        U2k = Uk*Vk
        V2k = Vk**2-2*Qk
        Uk = U2k%n
        Vk = V2k%n
        Qk = (Qk**2)%n
        k *= 2
        if char == '1':
            Uk1 = P*Uk+Vk
            Vk1 = D*Uk+P*Vk
            Uk1 = Uk1 if Uk1%2 == 0 else Uk1+n
            Vk1 = Vk1 if Vk1%2 == 0 else Vk1+n
            Uk = (Uk1//2)%n
            Vk = (Vk1//2)%n
            Qk = (Qk*Q)%n
            k += 1
    for i in range(diffl):
        if i == 0:
            if Uk%n == 0:
                return True
        if Vk%n == 0:
            return True
        U2k = Uk*Vk
        V2k = Vk**2-2*Qk
        Uk = U2k%n
        Vk = V2k%n
        Qk = (Qk**2)%n
        k *= 2
    return False

def _eff_route(d: int) -> list:
    eff_list = []
    first1 = True
    while d > 1:
        if d%2 == 0:
            d //= 2
            eff_list.append('2x')
        else:
            d -= 1
            if first1:
                eff_list.append('1+d')
                first1 = False
            else:
                eff_list.append('1+')
    return eff_list[::-1]

def isprime(n: int) -> bool:
    '''Checks n for primality using Baillie-PSW.'''
    if n <= 1:
        return False
    for i in one_and_two_digit_prime_numbers:
        if n%i == 0:
            if n/i == 1:
                return True
            else:
                return False
    if not miller_rabin(n, 2):
        return False
    if not lucasprime(n):
        return False
    return True
    
def _issq(n: int) -> bool:
    c = int(n**(1/2))
    return c**2 == n

def tdiv(n) -> bool:
    '''Performs trial division to determine primality. Fast for small numbers, but gets inefficient quickly.'''
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

        # Temporarily retired, runs too slowly for "small" sample sizes/N ( < 10000000)
# def genprimes(n) -> int:
#     '''Yields all primes less than or equal to n. Will yield nothing if n<2.'''
#     if n < 2:   return
#     yield 2
#     if n == 2:  return
#     for x in range(3,n+1,2):
#         if isprime(x):  yield x

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
    '''
    Returns the prime factorization of n. I plan to implement a more efficient
    algorithm at some point.
    '''
    if n<2:
        return []
    z=2
    lim = n**(1/2)
    pfacs=[]
    while not isprime(n):
        if(n%z==0):
            pfacs.append(z)
            n=n//z
        else:
            z+=1
    pfacs.append(n)
    return pfacs

def spfac(n) -> list:
    '''Returns the prime factorization of n as a set such that there are no duplicates.'''
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
##    for i in range(20000000000000000000000000000000000,20000000000000000000000000001000000):
##        isprime(i)
##        if i%100000 == 0:
##            print(i)
##    print(gl)
    while True:
        try:
            n=int(input())
            print(isprime(n))
        except ValueError:
            print('Invalid n')
