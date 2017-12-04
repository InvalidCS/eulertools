'''
Less efficient than the built-in pow function.
'''

def modpow(base: int, exp: int, mod: int) -> int:
    '''Returns (base**exp)%mod.'''
    s = bin(exp)[2:]
    print(s)
    s = s[::-1]
    result = 1
    a = base%mod
    for char in s:
##        print(char)
##        print(a)
        if char == '1':
            result = (result*a)%mod
##            print(result)
        a = (a**2)%mod
    return result

##def modpow(base: int, exp: int, mod: int) -> int:
##    '''Returns (base**exp)%mod.'''
##    res = 1
##    for a in range(exp):
##        res = (res*base)%mod
##    return res

if __name__ == '__main__':
    print(modpow(2,5873164042612555,48112959837082048697))
            
